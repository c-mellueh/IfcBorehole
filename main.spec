# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
added_files = [
    ('boreholeCreator', 'boreholeCreator'),
    (r'c:\Users\chris\Programmieren\IfcBorehole\.venv\Lib\site-packages\ifcopenshell\util', 'ifcopenshell/util')
]
hi = ['PySide6',
'pandas',
'ifcopenshell',
'numpy',
'geopandas',
'pyqtconsole',
'fiona',
'appdirs','ifcopenshell','ifcopenshell.util','ifcopenshell.util.element']
a = Analysis(
    ['boreholeGUI\\__main__.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=hi,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='IfcBorehole',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='boreholeGUI/icons/icon.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='IfcBorehole',
)
