; 该脚本使用 HM VNISEdit 脚本编辑器向导产生

; 安装程序初始定义常量
!define PRODUCT_NAME "住院错误项目删除工具"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "东方医院信息科"
!define PRODUCT_WEB_SITE "rajjim@github.com"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!insertmacro MUI_PAGE_FINISH

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\住院错误项目删除工具"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "东方医院"

Section "安装删除工具" SEC01
  SetOutPath "$INSTDIR\*.*"
  SetOverwrite ifnewer
  File /r "新建文件夹 (4)\dist\*.*"
SectionEnd

Section -AdditionalIcons
  SetOutPath $INSTDIR
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateDirectory "$SMPROGRAMS\住院错误项目删除工具"
  CreateShortCut "$SMPROGRAMS\住院错误项目删除工具\住院错误项目删除工具.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$SMPROGRAMS\住院错误项目删除工具\Uninstall.lnk" "$INSTDIR\uninst.exe"
  CreateShortCut "$DESKTOP\住院错误项目删除工具.lnk" "$INSTDIR\main.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  以下是安装程序的卸载部分  *
 ******************************/

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"

  Delete "$SMPROGRAMS\住院错误项目删除工具\住院错误项目删除工具.exe"
  Delete "$SMPROGRAMS\住院错误项目删除工具\Uninstall.lnk"
  Delete "$DESKTOP\住院错误项目删除工具.lnk"
  RMDir "$SMPROGRAMS\住院错误项目删除工具"

  RMDir /r "$INSTDIR\*.*"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  SetAutoClose true
SectionEnd

#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "您确实要完全移除 $(^Name) ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从您的计算机移除。"
FunctionEnd
