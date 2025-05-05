# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ['src/app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('models/waste_classifier.h5', 'models'),
        ('src/data/prepare_data.py', 'src/data'),
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageFile',
        'PIL.JpegImagePlugin',
        'PIL.PngImagePlugin',
        'PIL.BmpImagePlugin',
        'PIL.GifImagePlugin',
        'PIL.TiffImagePlugin',
        'numpy',
        'h5py',
        'tensorflow',
        'sklearn',
        'scipy',
    ],
    hookspath=[],
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
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
