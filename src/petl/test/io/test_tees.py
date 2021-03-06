# -*- coding: utf-8 -*-


from __future__ import absolute_import, print_function, division


__author__ = 'Alistair Miles <alimanfoo@googlemail.com>'


from tempfile import NamedTemporaryFile


from petl.testutils import ieq
import petl.fluent as etl


def test_teepickle():

    t1 = (('foo', 'bar'),
          ('a', 2),
          ('b', 1),
          ('c', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)
    etl.wrap(t1).teepickle(f1.name).selectgt('bar', 1).topickle(f2.name)

    ieq(t1, etl.frompickle(f1.name))
    ieq(etl.wrap(t1).selectgt('bar', 1), etl.frompickle(f2.name))


def test_teecsv():

    t1 = (('foo', 'bar'),
          ('a', 2),
          ('b', 1),
          ('c', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)

    etl.wrap(t1).teecsv(f1.name).selectgt('bar', 1).tocsv(f2.name)

    ieq(t1,
        etl.fromcsv(f1.name).convertnumbers())
    ieq(etl.wrap(t1).selectgt('bar', 1),
        etl.fromcsv(f2.name).convertnumbers())


def test_teetsv():

    t1 = (('foo', 'bar'),
          ('a', 2),
          ('b', 1),
          ('c', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)

    etl.wrap(t1).teetsv(f1.name).selectgt('bar', 1).totsv(f2.name)

    ieq(t1,
        etl.fromtsv(f1.name).convertnumbers())
    ieq(etl.wrap(t1).selectgt('bar', 1),
        etl.fromtsv(f2.name).convertnumbers())


def test_teeucsv():

    t1 = ((u'name', u'id'),
          (u'Արամ Խաչատրյան', 1),
          (u'Johann Strauß', 2),
          (u'Вагиф Сәмәдоғлу', 3),
          (u'章子怡', 4),
          )

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)

    etl.wrap(t1).teeucsv(f1.name).selectgt('id', 1).toucsv(f2.name)

    ieq(t1,
        etl.fromucsv(f1.name).convertnumbers())
    ieq(etl.wrap(t1).selectgt('id', 1),
        etl.fromucsv(f2.name).convertnumbers())


def test_teeutsv():

    t1 = ((u'name', u'id'),
          (u'Արամ Խաչատրյան', 1),
          (u'Johann Strauß', 2),
          (u'Вагиф Сәмәдоғлу', 3),
          (u'章子怡', 4),
          )

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)

    etl.wrap(t1).teeutsv(f1.name).selectgt('id', 1).toutsv(f2.name)

    ieq(t1,
        etl.fromutsv(f1.name).convertnumbers())
    ieq(etl.wrap(t1).selectgt('id', 1),
        etl.fromutsv(f2.name).convertnumbers())


def test_teetext():

    t1 = (('foo', 'bar'),
          ('a', 2),
          ('b', 1),
          ('c', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)

    prologue = 'foo,bar\n'
    template = '{foo},{bar}\n'
    epilogue = 'd,4'
    (etl
     .wrap(t1)
     .teetext(f1.name,
              template=template,
              prologue=prologue,
              epilogue=epilogue)
     .selectgt('bar', 1)
     .topickle(f2.name))

    ieq(t1 + (('d', 4),),
        etl.fromcsv(f1.name).convertnumbers())
    ieq(etl.wrap(t1).selectgt('bar', 1),
        etl.frompickle(f2.name))


def test_teeutext():

    t1 = ((u'foo', u'bar'),
          (u'Արամ Խաչատրյան', 2),
          (u'Johann Strauß', 1),
          (u'Вагиф Сәмәдоғлу', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)

    prologue = u'foo,bar\n'
    template = u'{foo},{bar}\n'
    epilogue = u'章子怡,4'
    (etl
     .wrap(t1)
     .teeutext(f1.name,
               template=template,
               prologue=prologue,
               epilogue=epilogue)
     .selectgt('bar', 1)
     .topickle(f2.name))

    ieq(t1 + ((u'章子怡', 4),),
        etl.fromucsv(f1.name).convertnumbers())
    ieq(etl.wrap(t1).selectgt('bar', 1),
        etl.frompickle(f2.name))


def test_teehtml():

    t1 = (('foo', 'bar'),
          ('a', 2),
          ('b', 1),
          ('c', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)
    etl.wrap(t1).teehtml(f1.name).selectgt('bar', 1).topickle(f2.name)

    ieq(t1, etl.fromxml(f1.name, './/tr', ('th', 'td')).convertnumbers())
    ieq(etl.wrap(t1).selectgt('bar', 1), etl.frompickle(f2.name))


def test_teeuhtml():

    t1 = ((u'foo', u'bar'),
          (u'Արամ Խաչատրյան', 2),
          (u'Johann Strauß', 1),
          (u'Вагиф Сәмәдоғлу', 3))

    f1 = NamedTemporaryFile(delete=False)
    f2 = NamedTemporaryFile(delete=False)
    etl.wrap(t1).teeuhtml(f1.name).selectgt('bar', 1).topickle(f2.name)

    ieq(t1, etl.fromxml(f1.name, './/tr', ('th', 'td')).convertnumbers())
    ieq(etl.wrap(t1).selectgt('bar', 1), etl.frompickle(f2.name))


