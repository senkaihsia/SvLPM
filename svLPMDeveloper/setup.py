from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], includes = ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'], excludes = [], bin_excludes = ["QtDesigner"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('svLPM.py', base=base)
]

setup(name='svLPM',
      version = '1.0',
      description = 'SimVascular Lumped Parameter Modeller',
      options = dict(build_exe = buildOptions),
      executables = executables)
