"""
======================
Appline Reports Framework V0.1 Beta - Based on Geraldo Reports
======================

Descripcion
--------

Apprework esta basado en Geraldo, con algunas modificaciones. Pensado para funcionar
ReportBuilder o QuickReport. Trabaja con bandas de ancho fijo y altura variable para
mostrar informacion  de tipo encabezado, sumario, detalles, agrupaciones, etc.

It is under GPL and works only with Django framework and Python language.

It depends on ReportLab library to work.

Packages Structure
------------------

- base.py - contains report base classes and definitions, including report,
  subreport, bands an groupping.

- barcodes.py - contains code related to render barcodes in reports.

- cache.py - contains settings and backend to store reports in cache.

- charts.py - contains code to make charts.

- cross_reference.py - contains the cross reference table matrix class.

- exceptions.py - contains Geraldo specific exceptions.

- graphics.py - contains graphic classes and definitions

- models.py - there is nothing. Just to be compatible with Django pluggable
  application structure and make possible run tests suite.

- widgets.py - contains widget classes and definitions.

- utils.py - contains useful functions, decorators and flags.

- generators - a package that contains generator classes.

- tests - a package with automated doc tests.
"""

from version import VERSION, get_version

__author__ = 'Jorge Riberi'
__license__ = 'GNU Lesser General Public License (LGPL)'
__url__ = 'http://geraldo.sourceforge.net/'
__version__ = get_version()

