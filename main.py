import sys
import os
import json
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QFile, QIODevice, QFileInfo
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import winreg as reg 
from ui_mainwindow import Ui_MainWindow
import tempfile

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Ui 클래스 상속
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # self.dir_path = os.path.dirname(os.path.realpath(__file__))
        
        self.progressbar = QProgressBar(self.statusbar)
        self.progressbar.setMaximumSize(180, 19)
        self.statusbar.addWidget(self.progressbar)

        self.from_folder_path = "C:/"
        self.to_folder_path = "C:/"
        self.brightness_factor = 50
        self.contrast_factor = 10
        self.sharpeness_factor = 0.3
        self.maxSize = 1.5

        key = reg.HKEY_CURRENT_USER 
        key_value = "Software\DIGIBOOK\SHARPENER"
        try:
            open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
            value, type = reg.QueryValueEx(open, "from")
            self.from_folder_path = str(value)
            value, type = reg.QueryValueEx(open, "to")
            self.to_folder_path = str(value)
            value, type = reg.QueryValueEx(open, "brightness")
            self.brightness_factor = float(value)
            value, type = reg.QueryValueEx(open, "contrast")
            self.contrast_factor = float(value)
            value, type = reg.QueryValueEx(open, "sharpeness")
            self.sharpeness_factor = float(value)
            value, type = reg.QueryValueEx(open, "maxsize")
            self.maxSize = float(value)
            
        except FileNotFoundError:
            open = reg.CreateKey(key, key_value)
            reg.SetValueEx(open, "from", 0, reg.REG_SZ, self.from_folder_path)
            reg.SetValueEx(open, "to", 0, reg.REG_SZ, self.to_folder_path)
            reg.SetValueEx(open, "brightness", 0, reg.REG_SZ, str(self.brightness_factor))
            reg.SetValueEx(open, "contrast", 0, reg.REG_SZ, str(self.contrast_factor))
            reg.SetValueEx(open, "sharpeness", 0, reg.REG_SZ, str(self.sharpeness_factor))
            reg.SetValueEx(open, "maxsize", 0, reg.REG_SZ, str(self.maxSize))
        
        self.editMax.setText(str(self.maxSize * 100.0))
        # 이미지 표시 영역
        self.imageLabel.setBackgroundRole(QPalette.ColorRole.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        # imageLabel.setScaledContents(True) 
        self.imageLabel1.setBackgroundRole(QPalette.ColorRole.Base)
        self.imageLabel1.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)

        self.scrollArea.setBackgroundRole(QPalette.ColorRole.Dark)
        self.scrollArea1.setBackgroundRole(QPalette.ColorRole.Dark)
        QScroller.grabGesture(self.scrollArea, QScroller.ScrollerGestureType.LeftMouseButtonGesture)
        # scrollArea.setVisible(False)

        # root_path = "C:/"
        self.from_file_system = QFileSystemModel()
        self.from_file_system.setRootPath(self.from_file_system.myComputer())
        self.from_file_system.setReadOnly(False)
        self.treeView.setModel(self.from_file_system)
        self.treeView.setCurrentIndex(self.from_file_system.index(self.from_folder_path))
        self.treeView.clicked.connect(lambda index : self.from_item_clicked(index))
        self.treeView.setDragEnabled(True)
        self.treeView.setColumnWidth(0, 300)
        self.from_item_clicked(self.from_file_system.index(self.from_folder_path))

        self.to_file_system = QFileSystemModel()
        self.to_file_system.setRootPath(self.to_file_system.myComputer())
        self.to_file_system.setReadOnly(False)
        self.treeView_2.setModel(self.to_file_system)
        self.treeView_2.setCurrentIndex(self.to_file_system.index(self.to_folder_path))
        self.treeView_2.clicked.connect(lambda index : self.to_item_clicked(index))
        self.treeView_2.setDragEnabled(True)
        self.treeView_2.setColumnWidth(0, 300)
        self.to_file_system.index(self.to_folder_path)
        self.treeView_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView_2.customContextMenuRequested.connect(self._show_context_menu)

        self.pbSharpen.clicked.connect(self.do_sharpen)
        
        self.pbTone.clicked.connect(self.do_Bright_Contrast)
        
        self.pushButton.clicked.connect(self.do_transform)
        
        self.editSharpen.setText(str(self.sharpeness_factor))
        self.sliderSharpen.setValue(self.sharpeness_factor*10.0)
        self.sliderSharpen.valueChanged.connect(lambda value : self.value_changed_sliderSharpen(value))
        self.editSharpen.textChanged.connect(lambda text : self.text_changed_editSharpen(text))    

        self.editBrightness.setText(str(self.brightness_factor))
        self.slideBrightness.setValue(self.brightness_factor)
        self.slideBrightness.valueChanged.connect(lambda value : self.value_changed_slideBrightness(value))
        self.editBrightness.textChanged.connect(lambda text : self.text_changed_editBrightness(text))    

        self.editContrast.setText(str(self.contrast_factor))
        self.sliderContrast.setValue(self.contrast_factor)
        self.sliderContrast.valueChanged.connect(lambda value : self.value_changed_sliderContrast(value))
        self.editContrast.textChanged.connect(lambda text : self.text_changed_editContrast(text))   
        self.editMax.textChanged.connect(lambda text: self.text_changed_editMax(text))
        
        self.scrollArea.verticalScrollBar().valueChanged.connect(lambda value : self.scroll_area_vertical_changed(value))
        self.scrollArea.horizontalScrollBar().valueChanged.connect(lambda value : self.scroll_area_horizontal_changed(value))
    
    def scroll_area_vertical_changed(self, value):
        self.scrollArea1.verticalScrollBar().setValue(value)
        
    def scroll_area_horizontal_changed(self, value):
        self.scrollArea1.horizontalScrollBar().setValue(value)      
        
    def display_current_image(self, file_path):
        reader = QImageReader(file_path)
        reader.setAutoTransform(True)
        newImage = QImage(reader.read())
        if newImage.isNull() == False:
            if newImage.colorSpace().isValid() :
                newImage.convertToColorSpace(QColorSpace.NamedColorSpace.SRgb)
            self.scrollArea.setWidgetResizable(True)
            self.imageLabel.setPixmap(QPixmap.fromImage(newImage))
            self.imageLabel.resize(self.imageLabel.pixmap().size())
            self.imageLabel.setFixedWidth(newImage.width())
            self.imageLabel.setFixedHeight(newImage.height())
            self.scrollArea.setVisible(True)
            
            self.current_image_path = file_path
            self.currentImage = True
            
            self.imageLabel1.clear()
            self.prevImage = False
            
    def from_item_clicked(self, index):
        indexItem = self.from_file_system.index(index.row(), 0, index.parent())
        self.from_file_name = self.from_file_system.fileName(indexItem)
        self.from_file_path = self.from_file_system.filePath(indexItem)
        self.from_is_dir = self.from_file_system.isDir(indexItem)

        if self.from_is_dir:
            # dir 인 경우 : 현재 경로를 저장한다
            self.from_folder_path = self.from_file_path
            
            self.imageLabel.clear()
            self.currentImage = False
            
            self.imageLabel1.clear()
            self.prevImage = False
        else:
            # file 인 경우 : 상위 폴더 경로를 저장한다
            self.from_folder_path = QFileInfo(self.from_file_path).absoluteDir().absolutePath()
            self.display_current_image(self.from_file_path)

        # # print(from_folder_path)
        self.saveSettings()

    def to_item_clicked(self, index):
        indexItem = self.to_file_system.index(index.row(), 0, index.parent())
        self.to_file_path = self.to_file_system.filePath(indexItem)
        self.to_is_dir = self.to_file_system.isDir(indexItem)

        if self.to_is_dir:
            # dir 인 경우 : 현재 경로를 저장한다
            self.to_folder_path = self.to_file_path
            
            self.imageLabel.clear()
            self.currentImage = False
            
            self.imageLabel1.clear()
            self.prevImage = False
        else:
            # file 인 경우 : 상위 폴더 경로를 저장한다
            self.to_folder_path = QFileInfo(self.to_file_path).absoluteDir().absolutePath()
            self.display_current_image(self.to_file_path)

        # print(to_folder_path)
        self.saveSettings()

    def saveSettings(self):
        key = reg.HKEY_CURRENT_USER 
        key_value = "Software\DIGIBOOK\SHARPENER"
        open = reg.CreateKey(key,key_value)
        reg.SetValueEx(open, "from", 0, reg.REG_SZ, self.from_folder_path)
        reg.SetValueEx(open, "to", 0, reg.REG_SZ, self.to_folder_path)
        reg.SetValueEx(open, "brightness", 0, reg.REG_SZ, str(self.brightness_factor))
        reg.SetValueEx(open, "contrast", 0, reg.REG_SZ, str(self.contrast_factor))
        reg.SetValueEx(open, "sharpeness", 0, reg.REG_SZ, str(self.sharpeness_factor))

    def do_transform(self):
        # 동일한 폴더인지 검사
        if self.from_folder_path == self.to_folder_path:
            buttonReply = QMessageBox.warning(
                self, '경고', "동일한 폴더가 지정되어 있어서, 원본 파일이 변경될 수 있습니다. 계속하시겠습니까?", 
                QMessageBox.Yes | QMessageBox.No, 
                QMessageBox.No
                )

            if buttonReply == QMessageBox.No:
                return
        
        transform_type = 0
        if self.cbTone.isChecked():
            transform_type = transform_type + 1
        if self.cbSharpen.isChecked():
            transform_type = transform_type + 2
            
        if transform_type == 0:
            QMessageBox.information(self, '확인', "선택된 변환 옵션이 없습니다.")
            return            
        
        if self.from_is_dir:
            # 폴더일 경우, 폴더 내 파일 및 하위 폴더 포함
            self.total_count = 0
            self.current_count = 0
            new_folder_name = os.path.basename(self.from_folder_path)
            self.do_process_dir(self.from_folder_path, self.to_folder_path + "/" + new_folder_name, transform_type)
            QMessageBox.information(self, '완료', "폴더 변환이 완료되었습니다.")
        else:
            self.do_process_file(self.from_folder_path, self.from_file_name, self.to_folder_path, transform_type)

    def do_sharpen(self):
        if self.currentImage:
            self.do_prev_file(1)
            
    def do_Bright_Contrast(self):
        if self.currentImage:
            self.do_prev_file(2)

    def do_process_dir(self, dir_path_from, dir_path_to, do_type):
        if not os.path.exists(dir_path_to):
            os.mkdir(dir_path_to)

        files = os.listdir(dir_path_from)
        self.total_count = self.total_count + len(files)
        self.progressbar.setMaximum(self.total_count)
        for file in files:
            self.current_count = self.current_count + 1
            self.progressbar.setValue(self.current_count)
            path = dir_path_from + '/' + file
            if os.path.isdir(path):
                self.do_process_dir(dir_path_from + '/' + file, dir_path_to + '/' + file, do_type)
            else:
                self.do_process_file(dir_path_from, file, dir_path_to, do_type)

    def do_process_file(self, dir_path_from, file_name, dir_path_to, do_type):
        prev_file_size = os.path.getsize(dir_path_from + '/' + file_name)
        img_array = np.fromfile(dir_path_from + '/' + file_name, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        prev_file_size = len(img_array)
        # image = cv2.imread(dir_path_from + '/' + file_name, flags=cv2.IMREAD_COLOR)
        if image is not None:
            if do_type == 1 or do_type == 3:
                alpha = self.contrast_factor / 10.0
                beta = self.brightness_factor
                adjusted = cv2.addWeighted(image, alpha, image, 0, beta)
                image = adjusted
                
            if do_type == 2 or do_type == 3:
                param = -self.sharpeness_factor
                param1 = 1 - (param*4)
                kernel = np.array([[0, param, 0],
                                [param, param1,param],
                                [0, param, 0]])
                image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
                image = image_sharp
                
            extention = os.path.splitext(file_name)[1]
            # 100부터 5씩 품질 감소
            jpg_quality = 100
            encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),jpg_quality]
            result, encoded_img = cv2.imencode(extention, image, encode_param)
            while len(encoded_img) > prev_file_size * self.maxSize:
                jpg_quality = jpg_quality - 5
                encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),jpg_quality]
                result, encoded_img = cv2.imencode(extention, image, encode_param)
            # 바로 전단계부터 1씩 품질 감소
            jpg_quality = jpg_quality + 5
            encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),jpg_quality]
            result, encoded_img = cv2.imencode(extention, image, encode_param)
            while len(encoded_img) > prev_file_size * self.maxSize:
                jpg_quality = jpg_quality - 1
                encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),jpg_quality]
                result, encoded_img = cv2.imencode(extention, image, encode_param)
                
            if result:
                with open(dir_path_to + '/' + file_name, mode='w+b') as f:
                    encoded_img.tofile(f)

            # cv2.imwrite(dir_path_to + '/' + file_name, adjusted)

    def show_prev(self, prev_data):
        current_file_name = os.path.basename(self.current_image_path)
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(temp_dir + '/' + current_file_name, mode='w+b') as f:
                prev_data.tofile(f)
            
            reader = QImageReader(temp_dir + '/' + current_file_name)
            reader.setAutoTransform(True)
            newImage = QImage(reader.read())
            if newImage.isNull() == False:
                if newImage.colorSpace().isValid() :
                    newImage.convertToColorSpace(QColorSpace.NamedColorSpace.SRgb)
                self.scrollArea1.setWidgetResizable(True)
                self.imageLabel1.setPixmap(QPixmap.fromImage(newImage))
                self.imageLabel1.resize(self.imageLabel1.pixmap().size())
                self.imageLabel1.setFixedWidth(newImage.width())
                self.imageLabel1.setFixedHeight(newImage.height())
                self.scrollArea1.setVisible(True)
                self.prevImage = True
            reader = None

    def do_prev_file(self, do_type):
        img_array = np.fromfile(self.current_image_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # image = cv2.imread(dir_path_from + '/' + file_name, flags=cv2.IMREAD_COLOR)
        if image is not None:
            if do_type == 1:
                param = -self.sharpeness_factor
                param1 = 1 - (param*4)
                kernel = np.array([[0, param, 0],
                                [param, param1,param],
                                [0, param, 0]])
                image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
                extention = os.path.splitext(self.current_image_path)[1]
                result, encoded_img = cv2.imencode(extention, image_sharp)
                if result:
                    self.show_prev(encoded_img)

                # cv2.imwrite(dir_path_to + '/' + file_name, image_sharp)
            elif do_type == 2:
                alpha = self.contrast_factor / 10.0
                beta = self.brightness_factor
                adjusted = cv2.addWeighted(image, alpha, image, 0, beta)
                extention = os.path.splitext(self.current_image_path)[1]
                result, encoded_img = cv2.imencode(extention, adjusted)
                if result:
                    self.show_prev(encoded_img)

    def _show_context_menu(self, position):
            display_action1 = QAction("New Folder")
            display_action1.triggered.connect(self.toNewFolder)
            menu = QMenu(self.treeView_2)
            menu.addAction(display_action1)        
            menu.exec(self.treeView_2.mapToGlobal(position))
            
    def toNewFolder(self):
        new_path = self.to_folder_path + '/new folder'
        if not os.path.exists(new_path):
            os.mkdir(new_path)
            
    def value_changed_sliderSharpen(self, value):
        self.sharpeness_factor = value / 10.0
        self.editSharpen.setText(str(self.sharpeness_factor))
        
    def text_changed_editSharpen(self, text):
        self.sharpeness_factor = float(text)
        self.sliderSharpen.setValue(self.sharpeness_factor*10.0)    

    def value_changed_slideBrightness(self, value):
        self.brightness_factor = value
        self.editBrightness.setText(str(self.brightness_factor))
        
    def text_changed_editBrightness(self, text):
        self.brightness_factor = float(text)
        self.slideBrightness.setValue(self.brightness_factor)    

    def value_changed_sliderContrast(self, value):
        self.contrast_factor = value
        self.editContrast.setText(str(self.contrast_factor))
        
    def text_changed_editContrast(self, text):
        self.contrast_factor = float(text)
        self.sliderContrast.setValue(self.contrast_factor)
        
    def text_changed_editMax(self, text):
        self.maxSize = float(text) / 100.0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
