# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['1.ico', '小窗口.py', '我们走过的路.py', '回忆相册.py', '恋爱画板.py', '恋爱画板2.py', '恋爱画板3.py', '我们的故事呀.py'],
    pathex=['D:\\pyqt555\\Lib\\site-packages\\PyQt5\\Qt5\\bin'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Kitty',
)
