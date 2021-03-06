#Tensor Contraction Engine Configuration Interaction (CI) energies: SD, SDT, SDTQ 
import os
import sys
from ..addons import *
from ..utils import *
import qcdb

h2o = qcdb.set_molecule('''
        O      0.000000000000     0.000000000000    -0.123909374404
        H      0.000000000000     1.429936611037     0.983265845431
        H      0.000000000000    -1.429936611037     0.983265845431
        ''')

print(h2o)

def check_cisd(return_value):
    hf           =   -74.506112017320
    cisd_tot     =   -74.746025986067849
    cisd_corl    =    -0.239913968748276   

    assert compare_values(hf, qcdb.get_variable('HF TOTAL ENERGY'), 5, 'hf ref')
    assert compare_values(cisd_tot, qcdb.get_variable('CISD TOTAL ENERGY'), 5, 'cisd tot')
    assert compare_values(cisd_corl, qcdb.get_variable('CISD CORRELATION ENERGY'), 5, 'cisd corl')

@using_nwchem
def test_1_cisd():
    qcdb.set_options({
        'basis' : 'sto-3g',
        'qc_module': 'TCE',
        'nwchem_tce__cisd'    : True,
        'memory': '1000 mb'
        })
    val = qcdb.energy('nwc-cisd')
    check_cisd(val)

def check_cisdt(return_value):
    hf           =   -74.506112017320
    cisdt_tot    =   -74.746791001337797
    cisdt_corl   =    -0.240678984018215

    assert compare_values(hf, qcdb.get_variable('HF TOTAL ENERGY'), 5, 'hf ref')
    assert compare_values(cisdt_tot, qcdb.get_variable('CISDT TOTAL ENERGY'), 5, 'cisdt tot')
    assert compare_values(cisdt_corl, qcdb.get_variable('CISDT CORRELATION ENERGY'), 5, 'cisdt corl')

@using_nwchem
def test_2_cisdt():
    qcdb.set_options({
        'basis' : 'sto-3g',
        'qc_module': 'TCE',
        'nwchem_tce__cisdt'    : True,
        'memory': '1000 mb'
        })
    val = qcdb.energy('nwc-cisdt')
    check_cisdt(val)


def check_cisdtq(return_value):
    hf           =   -74.506112017320
    cisdtq_tot   =   -74.788955327897597
    cisdtq_corl  =    -0.282843310578009

    assert compare_values(hf, qcdb.get_variable('HF TOTAL ENERGY'), 5, 'hf ref')
    assert compare_values(cisdtq_tot, qcdb.get_variable('CISDTQ TOTAL ENERGY'), 5, 'cisdtq tot')
    assert compare_values(cisdtq_corl, qcdb.get_variable('CISDTQ CORRELATION ENERGY'), 5, 'cisdtq corl')

@using_nwchem
def test_3_cisdtq():
    qcdb.set_options({
        'basis' : 'sto-3g',
        'qc_module': 'TCE',
        'nwchem_tce__cisdtq'    : True,
        'memory': '1000 mb'
        })
    val = qcdb.energy('nwc-cisdtq')
    check_cisdtq(val)

