# -*- coding: mbcs -*-
# tlb file generated from:
# C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat x86
# midl C:\Program Files (x86)\Windows Kits\10\Include\10.0.15063.0\um\ShObjIdl_core.idl
typelib_path = 'C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.15063.0\\um\\ShObjIdl_core.tlb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import IUnknown
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
WSTRING = c_wchar_p
from comtypes import CoClass
from comtypes.typeinfo import ITypeComp
from comtypes.automation import IDispatch
from comtypes.typeinfo import tagVARKIND
from comtypes.typeinfo import tagSAFEARRAYBOUND
from ctypes.wintypes import tagSIZE
from ctypes.wintypes import _POINTL
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import SCODE
from ctypes.wintypes import _FILETIME
from comtypes import BSTR
STRING = c_char_p
from comtypes.automation import DECIMAL
from comtypes.typeinfo import ULONG_PTR
from comtypes import wireHWND
from comtypes import IPersist
from ctypes.wintypes import tagRECT
from comtypes import tagBIND_OPTS2
from comtypes.typeinfo import tagDESCKIND
from comtypes.typeinfo import tagFUNCDESC
from comtypes import _COAUTHIDENTITY
from comtypes.typeinfo import tagELEMDESC
from comtypes import _COAUTHINFO
from comtypes.typeinfo import tagFUNCKIND
from comtypes.typeinfo import tagPARAMDESC
from comtypes.typeinfo import ITypeLib
from comtypes.automation import DECIMAL
from comtypes.typeinfo import tagPARAMDESCEX
UINT_PTR = c_ulong
LONG_PTR = c_int
from comtypes.automation import tagINVOKEKIND
from comtypes.typeinfo import tagCALLCONV
from comtypes.typeinfo import tagVARDESC
from comtypes.typeinfo import tagTLIBATTR
from comtypes import tagBIND_OPTS2
from comtypes.automation import VARIANT
from comtypes.typeinfo import tagSYSKIND
from comtypes.typeinfo import tagTYPEATTR
from comtypes.typeinfo import IRecordInfo
from ctypes.wintypes import tagRECT
from ctypes.wintypes import tagPOINT
from comtypes import _COSERVERINFO
from comtypes.typeinfo import ITypeInfo
from comtypes.typeinfo import tagTYPEKIND
from ctypes.wintypes import DWORD
from comtypes.typeinfo import tagTYPEDESC
from comtypes.typeinfo import tagIDLDESC
from comtypes.typeinfo import tagARRAYDESC
from comtypes.automation import VARIANT



# values for enumeration 'ASSOCIATIONLEVEL'
AL_MACHINE = 0
AL_EFFECTIVE = 1
AL_USER = 2
ASSOCIATIONLEVEL = c_int # enum
class IOpenControlPanel(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D11AD862-66DE-4DF4-BF6C-1F5621996AF1}')
    _idlflags_ = []

# values for enumeration 'CPVIEW'
CPVIEW_CLASSIC = 0
CPVIEW_ALLITEMS = 0
CPVIEW_CATEGORY = 1
CPVIEW_HOME = 1
CPVIEW = c_int # enum
IOpenControlPanel._methods_ = [
    COMMETHOD([], HRESULT, 'Open',
              ( ['in'], WSTRING, 'pszName' ),
              ( ['in'], WSTRING, 'pszPage' ),
              ( ['in'], POINTER(IUnknown), 'punkSite' )),
    COMMETHOD([], HRESULT, 'GetPath',
              ( ['in'], WSTRING, 'pszName' ),
              ( ['out'], WSTRING, 'pszPath' ),
              ( ['in'], c_uint, 'cchPath' )),
    COMMETHOD([], HRESULT, 'GetCurrentView',
              ( ['out'], POINTER(CPVIEW), 'pView' )),
]
################################################################
## code template for IOpenControlPanel implementation
##class IOpenControlPanel_Impl(object):
##    def Open(self, pszName, pszPage, punkSite):
##        '-no docstring-'
##        #return
##
##    def GetPath(self, pszName, cchPath):
##        '-no docstring-'
##        #return pszPath
##
##    def GetCurrentView(self):
##        '-no docstring-'
##        #return pView
##

class SearchFolderItemFactory(CoClass):
    _reg_clsid_ = GUID('{14010E02-BBBD-41F0-88E3-EDA371216584}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class ISearchFolderItemFactory(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A0FFBC28-5482-4366-BE27-3E81E78E06C2}')
    _idlflags_ = []
SearchFolderItemFactory._com_interfaces_ = [ISearchFolderItemFactory]

class IEnumObjects(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2C1C7E2E-2D0E-4059-831E-1E6F82335C2E}')
    _idlflags_ = []
IEnumObjects._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumObjects)), 'ppenum' )),
]
################################################################
## code template for IEnumObjects implementation
##class IEnumObjects_Impl(object):
##    def RemoteNext(self, celt, riid):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class OpenControlPanel(CoClass):
    _reg_clsid_ = GUID('{06622D85-6856-4460-8DE1-A81921B41C4B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
OpenControlPanel._com_interfaces_ = [IOpenControlPanel]

class IApplicationActivationManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2E941141-7F97-4756-BA1D-9DECDE894A3D}')
    _idlflags_ = []

# values for enumeration 'ACTIVATEOPTIONS'
AO_NONE = 0
AO_DESIGNMODE = 1
AO_NOERRORUI = 2
AO_NOSPLASHSCREEN = 4
AO_PRELAUNCH = 33554432
ACTIVATEOPTIONS = c_int # enum
class IShellItemArray(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B63EA76D-1F85-456F-A19C-48159EFA858B}')
    _idlflags_ = []
IApplicationActivationManager._methods_ = [
    COMMETHOD([], HRESULT, 'ActivateApplication',
              ( ['in'], WSTRING, 'appUserModelId' ),
              ( ['in'], WSTRING, 'arguments' ),
              ( ['in'], ACTIVATEOPTIONS, 'options' ),
              ( ['out'], POINTER(c_ulong), 'processId' )),
    COMMETHOD([], HRESULT, 'ActivateForFile',
              ( ['in'], WSTRING, 'appUserModelId' ),
              ( ['in'], POINTER(IShellItemArray), 'itemArray' ),
              ( ['in'], WSTRING, 'verb' ),
              ( ['out'], POINTER(c_ulong), 'processId' )),
    COMMETHOD([], HRESULT, 'ActivateForProtocol',
              ( ['in'], WSTRING, 'appUserModelId' ),
              ( ['in'], POINTER(IShellItemArray), 'itemArray' ),
              ( ['out'], POINTER(c_ulong), 'processId' )),
]
################################################################
## code template for IApplicationActivationManager implementation
##class IApplicationActivationManager_Impl(object):
##    def ActivateApplication(self, appUserModelId, arguments, options):
##        '-no docstring-'
##        #return processId
##
##    def ActivateForFile(self, appUserModelId, itemArray, verb):
##        '-no docstring-'
##        #return processId
##
##    def ActivateForProtocol(self, appUserModelId, itemArray):
##        '-no docstring-'
##        #return processId
##

class KnownFolderManager(CoClass):
    _reg_clsid_ = GUID('{4DF0C730-DF9D-4AE3-9153-AA6B82E9795A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IKnownFolderManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8BE2D872-86AA-4D47-B776-32CCA40C7018}')
    _idlflags_ = []
KnownFolderManager._com_interfaces_ = [IKnownFolderManager]


# values for enumeration 'FOLDERLOGICALVIEWMODE'
FLVM_UNSPECIFIED = -1
FLVM_FIRST = 1
FLVM_DETAILS = 1
FLVM_TILES = 2
FLVM_ICONS = 3
FLVM_LIST = 4
FLVM_CONTENT = 5
FLVM_LAST = 5
FOLDERLOGICALVIEWMODE = c_int # enum
class _tagpropertykey(Structure):
    pass
class SORTCOLUMN(Structure):
    pass
class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []
class ICondition(IPersistStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0FC988D4-C935-4B97-A973-46282EA175C8}')
    _idlflags_ = []
class _BYTE_BLOB(Structure):
    pass
wirePIDL = POINTER(_BYTE_BLOB)
ISearchFolderItemFactory._methods_ = [
    COMMETHOD([], HRESULT, 'SetDisplayName',
              ( ['in'], WSTRING, 'pszDisplayName' )),
    COMMETHOD([], HRESULT, 'SetFolderTypeID',
              ( ['in'], GUID, 'ftid' )),
    COMMETHOD([], HRESULT, 'SetFolderLogicalViewMode',
              ( ['in'], FOLDERLOGICALVIEWMODE, 'flvm' )),
    COMMETHOD([], HRESULT, 'SetIconSize',
              ( ['in'], c_int, 'iIconSize' )),
    COMMETHOD([], HRESULT, 'SetVisibleColumns',
              ( ['in'], c_uint, 'cVisibleColumns' ),
              ( ['in'], POINTER(_tagpropertykey), 'rgKey' )),
    COMMETHOD([], HRESULT, 'SetSortColumns',
              ( ['in'], c_uint, 'cSortColumns' ),
              ( ['in'], POINTER(SORTCOLUMN), 'rgSortColumns' )),
    COMMETHOD([], HRESULT, 'SetGroupColumn',
              ( ['in'], POINTER(_tagpropertykey), 'keyGroup' )),
    COMMETHOD([], HRESULT, 'SetStacks',
              ( ['in'], c_uint, 'cStackKeys' ),
              ( ['in'], POINTER(_tagpropertykey), 'rgStackKeys' )),
    COMMETHOD([], HRESULT, 'SetScope',
              ( ['in'], POINTER(IShellItemArray), 'psiaScope' )),
    COMMETHOD([], HRESULT, 'SetCondition',
              ( ['in'], POINTER(ICondition), 'pCondition' )),
    COMMETHOD([], HRESULT, 'GetShellItem',
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetIDList',
              ( ['out'], POINTER(wirePIDL), 'ppidl' )),
]
################################################################
## code template for ISearchFolderItemFactory implementation
##class ISearchFolderItemFactory_Impl(object):
##    def SetDisplayName(self, pszDisplayName):
##        '-no docstring-'
##        #return
##
##    def SetFolderTypeID(self, ftid):
##        '-no docstring-'
##        #return
##
##    def SetFolderLogicalViewMode(self, flvm):
##        '-no docstring-'
##        #return
##
##    def SetIconSize(self, iIconSize):
##        '-no docstring-'
##        #return
##
##    def SetVisibleColumns(self, cVisibleColumns, rgKey):
##        '-no docstring-'
##        #return
##
##    def SetSortColumns(self, cSortColumns, rgSortColumns):
##        '-no docstring-'
##        #return
##
##    def SetGroupColumn(self, keyGroup):
##        '-no docstring-'
##        #return
##
##    def SetStacks(self, cStackKeys, rgStackKeys):
##        '-no docstring-'
##        #return
##
##    def SetScope(self, psiaScope):
##        '-no docstring-'
##        #return
##
##    def SetCondition(self, pCondition):
##        '-no docstring-'
##        #return
##
##    def GetShellItem(self, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetIDList(self):
##        '-no docstring-'
##        #return ppidl
##

class ApplicationDesignModeSettings(CoClass):
    _reg_clsid_ = GUID('{958A6FB5-DCB2-4FAF-AAFD-7FB054AD1A3B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IApplicationDesignModeSettings(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2A3DEE9A-E31D-46D6-8508-BCC597DB3557}')
    _idlflags_ = []
class IApplicationDesignModeSettings2(IApplicationDesignModeSettings):
    _case_insensitive_ = True
    _iid_ = GUID('{490514E1-675A-4D6E-A58D-E54901B4CA2F}')
    _idlflags_ = []
ApplicationDesignModeSettings._com_interfaces_ = [IApplicationDesignModeSettings2]

class _wireSAFEARRAY_UNION(Structure):
    pass
class __MIDL_IOleAutomationTypes_0001(Union):
    pass
class _wireSAFEARR_BSTR(Structure):
    pass
class _FLAGGED_WORD_BLOB(Structure):
    pass
_wireSAFEARR_BSTR._fields_ = [
    ('Size', c_ulong),
    ('aBstr', POINTER(POINTER(_FLAGGED_WORD_BLOB))),
]
assert sizeof(_wireSAFEARR_BSTR) == 8, sizeof(_wireSAFEARR_BSTR)
assert alignment(_wireSAFEARR_BSTR) == 4, alignment(_wireSAFEARR_BSTR)
class _wireSAFEARR_UNKNOWN(Structure):
    pass
_wireSAFEARR_UNKNOWN._fields_ = [
    ('Size', c_ulong),
    ('apUnknown', POINTER(POINTER(IUnknown))),
]
assert sizeof(_wireSAFEARR_UNKNOWN) == 8, sizeof(_wireSAFEARR_UNKNOWN)
assert alignment(_wireSAFEARR_UNKNOWN) == 4, alignment(_wireSAFEARR_UNKNOWN)
class _wireSAFEARR_DISPATCH(Structure):
    pass
_wireSAFEARR_DISPATCH._fields_ = [
    ('Size', c_ulong),
    ('apDispatch', POINTER(POINTER(IDispatch))),
]
assert sizeof(_wireSAFEARR_DISPATCH) == 8, sizeof(_wireSAFEARR_DISPATCH)
assert alignment(_wireSAFEARR_DISPATCH) == 4, alignment(_wireSAFEARR_DISPATCH)
class _wireSAFEARR_VARIANT(Structure):
    pass
class _wireVARIANT(Structure):
    pass
_wireSAFEARR_VARIANT._fields_ = [
    ('Size', c_ulong),
    ('aVariant', POINTER(POINTER(_wireVARIANT))),
]
assert sizeof(_wireSAFEARR_VARIANT) == 8, sizeof(_wireSAFEARR_VARIANT)
assert alignment(_wireSAFEARR_VARIANT) == 4, alignment(_wireSAFEARR_VARIANT)
class _wireSAFEARR_BRECORD(Structure):
    pass
class _wireBRECORD(Structure):
    pass
_wireSAFEARR_BRECORD._fields_ = [
    ('Size', c_ulong),
    ('aRecord', POINTER(POINTER(_wireBRECORD))),
]
assert sizeof(_wireSAFEARR_BRECORD) == 8, sizeof(_wireSAFEARR_BRECORD)
assert alignment(_wireSAFEARR_BRECORD) == 4, alignment(_wireSAFEARR_BRECORD)
class _wireSAFEARR_HAVEIID(Structure):
    pass
_wireSAFEARR_HAVEIID._fields_ = [
    ('Size', c_ulong),
    ('apUnknown', POINTER(POINTER(IUnknown))),
    ('iid', GUID),
]
assert sizeof(_wireSAFEARR_HAVEIID) == 24, sizeof(_wireSAFEARR_HAVEIID)
assert alignment(_wireSAFEARR_HAVEIID) == 4, alignment(_wireSAFEARR_HAVEIID)
class _BYTE_SIZEDARR(Structure):
    pass
_BYTE_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ubyte)),
]
assert sizeof(_BYTE_SIZEDARR) == 8, sizeof(_BYTE_SIZEDARR)
assert alignment(_BYTE_SIZEDARR) == 4, alignment(_BYTE_SIZEDARR)
class _SHORT_SIZEDARR(Structure):
    pass
_SHORT_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ushort)),
]
assert sizeof(_SHORT_SIZEDARR) == 8, sizeof(_SHORT_SIZEDARR)
assert alignment(_SHORT_SIZEDARR) == 4, alignment(_SHORT_SIZEDARR)
class _LONG_SIZEDARR(Structure):
    pass
_LONG_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ulong)),
]
assert sizeof(_LONG_SIZEDARR) == 8, sizeof(_LONG_SIZEDARR)
assert alignment(_LONG_SIZEDARR) == 4, alignment(_LONG_SIZEDARR)
class _HYPER_SIZEDARR(Structure):
    pass
_HYPER_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_longlong)),
]
assert sizeof(_HYPER_SIZEDARR) == 8, sizeof(_HYPER_SIZEDARR)
assert alignment(_HYPER_SIZEDARR) == 4, alignment(_HYPER_SIZEDARR)
__MIDL_IOleAutomationTypes_0001._fields_ = [
    ('BstrStr', _wireSAFEARR_BSTR),
    ('UnknownStr', _wireSAFEARR_UNKNOWN),
    ('DispatchStr', _wireSAFEARR_DISPATCH),
    ('VariantStr', _wireSAFEARR_VARIANT),
    ('RecordStr', _wireSAFEARR_BRECORD),
    ('HaveIidStr', _wireSAFEARR_HAVEIID),
    ('ByteStr', _BYTE_SIZEDARR),
    ('WordStr', _SHORT_SIZEDARR),
    ('LongStr', _LONG_SIZEDARR),
    ('HyperStr', _HYPER_SIZEDARR),
]
assert sizeof(__MIDL_IOleAutomationTypes_0001) == 24, sizeof(__MIDL_IOleAutomationTypes_0001)
assert alignment(__MIDL_IOleAutomationTypes_0001) == 4, alignment(__MIDL_IOleAutomationTypes_0001)
_wireSAFEARRAY_UNION._fields_ = [
    ('sfType', c_ulong),
    ('u', __MIDL_IOleAutomationTypes_0001),
]
assert sizeof(_wireSAFEARRAY_UNION) == 28, sizeof(_wireSAFEARRAY_UNION)
assert alignment(_wireSAFEARRAY_UNION) == 4, alignment(_wireSAFEARRAY_UNION)
class _userHMETAFILEPICT(Structure):
    pass
class __MIDL_IWinTypes_0005(Union):
    pass
class _remoteMETAFILEPICT(Structure):
    pass
__MIDL_IWinTypes_0005._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_remoteMETAFILEPICT)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0005) == 8, sizeof(__MIDL_IWinTypes_0005)
assert alignment(__MIDL_IWinTypes_0005) == 8, alignment(__MIDL_IWinTypes_0005)
_userHMETAFILEPICT._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0005),
]
assert sizeof(_userHMETAFILEPICT) == 16, sizeof(_userHMETAFILEPICT)
assert alignment(_userHMETAFILEPICT) == 8, alignment(_userHMETAFILEPICT)
class KNOWNFOLDER_DEFINITION(Structure):
    pass

# values for enumeration 'KF_CATEGORY'
KF_CATEGORY_VIRTUAL = 1
KF_CATEGORY_FIXED = 2
KF_CATEGORY_COMMON = 3
KF_CATEGORY_PERUSER = 4
KF_CATEGORY = c_int # enum
KNOWNFOLDER_DEFINITION._fields_ = [
    ('category', KF_CATEGORY),
    ('pszName', WSTRING),
    ('pszDescription', WSTRING),
    ('fidParent', GUID),
    ('pszRelativePath', WSTRING),
    ('pszParsingName', WSTRING),
    ('pszToolTip', WSTRING),
    ('pszLocalizedName', WSTRING),
    ('pszIcon', WSTRING),
    ('pszSecurity', WSTRING),
    ('dwAttributes', c_ulong),
    ('kfdFlags', c_ulong),
    ('ftidType', GUID),
]
assert sizeof(KNOWNFOLDER_DEFINITION) == 76, sizeof(KNOWNFOLDER_DEFINITION)
assert alignment(KNOWNFOLDER_DEFINITION) == 4, alignment(KNOWNFOLDER_DEFINITION)

# values for enumeration 'DEVICE_SCALE_FACTOR'
DEVICE_SCALE_FACTOR_INVALID = 0
SCALE_100_PERCENT = 100
SCALE_120_PERCENT = 120
SCALE_125_PERCENT = 125
SCALE_140_PERCENT = 140
SCALE_150_PERCENT = 150
SCALE_160_PERCENT = 160
SCALE_175_PERCENT = 175
SCALE_180_PERCENT = 180
SCALE_200_PERCENT = 200
SCALE_225_PERCENT = 225
SCALE_250_PERCENT = 250
SCALE_300_PERCENT = 300
SCALE_350_PERCENT = 350
SCALE_400_PERCENT = 400
SCALE_450_PERCENT = 450
SCALE_500_PERCENT = 500
DEVICE_SCALE_FACTOR = c_int # enum

# values for enumeration 'APPLICATION_VIEW_STATE'
AVS_FULLSCREEN_LANDSCAPE = 0
AVS_FILLED = 1
AVS_SNAPPED = 2
AVS_FULLSCREEN_PORTRAIT = 3
APPLICATION_VIEW_STATE = c_int # enum

# values for enumeration 'EDGE_GESTURE_KIND'
EGK_TOUCH = 0
EGK_KEYBOARD = 1
EGK_MOUSE = 2
EDGE_GESTURE_KIND = c_int # enum
IApplicationDesignModeSettings._methods_ = [
    COMMETHOD([], HRESULT, 'SetNativeDisplaySize',
              ( ['in'], tagSIZE, 'nativeDisplaySizePixels' )),
    COMMETHOD([], HRESULT, 'SetScaleFactor',
              ( ['in'], DEVICE_SCALE_FACTOR, 'scaleFactor' )),
    COMMETHOD([], HRESULT, 'SetApplicationViewState',
              ( ['in'], APPLICATION_VIEW_STATE, 'viewState' )),
    COMMETHOD([], HRESULT, 'ComputeApplicationSize',
              ( ['out'], POINTER(tagSIZE), 'applicationSizePixels' )),
    COMMETHOD([], HRESULT, 'IsApplicationViewStateSupported',
              ( ['in'], APPLICATION_VIEW_STATE, 'viewState' ),
              ( ['in'], tagSIZE, 'nativeDisplaySizePixels' ),
              ( ['in'], DEVICE_SCALE_FACTOR, 'scaleFactor' ),
              ( ['out'], POINTER(c_int), 'supported' )),
    COMMETHOD([], HRESULT, 'TriggerEdgeGesture',
              ( ['in'], EDGE_GESTURE_KIND, 'edgeGestureKind' )),
]
################################################################
## code template for IApplicationDesignModeSettings implementation
##class IApplicationDesignModeSettings_Impl(object):
##    def SetNativeDisplaySize(self, nativeDisplaySizePixels):
##        '-no docstring-'
##        #return
##
##    def SetScaleFactor(self, scaleFactor):
##        '-no docstring-'
##        #return
##
##    def SetApplicationViewState(self, viewState):
##        '-no docstring-'
##        #return
##
##    def ComputeApplicationSize(self):
##        '-no docstring-'
##        #return applicationSizePixels
##
##    def IsApplicationViewStateSupported(self, viewState, nativeDisplaySizePixels, scaleFactor):
##        '-no docstring-'
##        #return supported
##
##    def TriggerEdgeGesture(self, edgeGestureKind):
##        '-no docstring-'
##        #return
##

class IObjectWithPropertyKey(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{FC0CA0A7-C316-4FD2-9031-3E628E6D4F23}')
    _idlflags_ = []
class IPropertyChange(IObjectWithPropertyKey):
    _case_insensitive_ = True
    _iid_ = GUID('{F917BC8A-1BBA-4478-A245-1BDE03EB9431}')
    _idlflags_ = []
IObjectWithPropertyKey._methods_ = [
    COMMETHOD([], HRESULT, 'SetPropertyKey',
              ( ['in'], POINTER(_tagpropertykey), 'key' )),
    COMMETHOD([], HRESULT, 'GetPropertyKey',
              ( ['out'], POINTER(_tagpropertykey), 'pkey' )),
]
################################################################
## code template for IObjectWithPropertyKey implementation
##class IObjectWithPropertyKey_Impl(object):
##    def SetPropertyKey(self, key):
##        '-no docstring-'
##        #return
##
##    def GetPropertyKey(self):
##        '-no docstring-'
##        #return pkey
##

class tag_inner_PROPVARIANT(Structure):
    pass
IPropertyChange._methods_ = [
    COMMETHOD([], HRESULT, 'ApplyToPropVariant',
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'propvarIn' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'ppropvarOut' )),
]
################################################################
## code template for IPropertyChange implementation
##class IPropertyChange_Impl(object):
##    def ApplyToPropVariant(self, propvarIn):
##        '-no docstring-'
##        #return ppropvarOut
##

class IDropTarget(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000122-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IDataObject(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000010E-0000-0000-C000-000000000046}')
    _idlflags_ = []
IDropTarget._methods_ = [
    COMMETHOD([], HRESULT, 'DragEnter',
              ( ['in'], POINTER(IDataObject), 'pDataObj' ),
              ( ['in'], c_ulong, 'grfKeyState' ),
              ( ['in'], _POINTL, 'pt' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwEffect' )),
    COMMETHOD([], HRESULT, 'DragOver',
              ( ['in'], c_ulong, 'grfKeyState' ),
              ( ['in'], _POINTL, 'pt' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwEffect' )),
    COMMETHOD([], HRESULT, 'DragLeave'),
    COMMETHOD([], HRESULT, 'Drop',
              ( ['in'], POINTER(IDataObject), 'pDataObj' ),
              ( ['in'], c_ulong, 'grfKeyState' ),
              ( ['in'], _POINTL, 'pt' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwEffect' )),
]
################################################################
## code template for IDropTarget implementation
##class IDropTarget_Impl(object):
##    def DragEnter(self, pDataObj, grfKeyState, pt):
##        '-no docstring-'
##        #return pdwEffect
##
##    def DragOver(self, grfKeyState, pt):
##        '-no docstring-'
##        #return pdwEffect
##
##    def DragLeave(self):
##        '-no docstring-'
##        #return
##
##    def Drop(self, pDataObj, grfKeyState, pt):
##        '-no docstring-'
##        #return pdwEffect
##

class ISequentialStream(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

class __MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001(Union):
    pass
class tagCLIPDATA(Structure):
    pass
class tagBSTRBLOB(Structure):
    pass
tagBSTRBLOB._fields_ = [
    ('cbSize', c_ulong),
    ('pData', POINTER(c_ubyte)),
]
assert sizeof(tagBSTRBLOB) == 8, sizeof(tagBSTRBLOB)
assert alignment(tagBSTRBLOB) == 4, alignment(tagBSTRBLOB)
class tagBLOB(Structure):
    pass
tagBLOB._fields_ = [
    ('cbSize', c_ulong),
    ('pBlobData', POINTER(c_ubyte)),
]
assert sizeof(tagBLOB) == 8, sizeof(tagBLOB)
assert alignment(tagBLOB) == 4, alignment(tagBLOB)
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IStorage(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000B-0000-0000-C000-000000000046}')
    _idlflags_ = []
class tagVersionedStream(Structure):
    pass
class _wireSAFEARRAY(Structure):
    pass
wirePSAFEARRAY = POINTER(POINTER(_wireSAFEARRAY))
class tagCAC(Structure):
    pass
tagCAC._fields_ = [
    ('cElems', c_ulong),
    ('pElems', STRING),
]
assert sizeof(tagCAC) == 8, sizeof(tagCAC)
assert alignment(tagCAC) == 4, alignment(tagCAC)
class tagCAUB(Structure):
    pass
tagCAUB._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ubyte)),
]
assert sizeof(tagCAUB) == 8, sizeof(tagCAUB)
assert alignment(tagCAUB) == 4, alignment(tagCAUB)
class tagCAI(Structure):
    pass
tagCAI._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_short)),
]
assert sizeof(tagCAI) == 8, sizeof(tagCAI)
assert alignment(tagCAI) == 4, alignment(tagCAI)
class tagCAUI(Structure):
    pass
tagCAUI._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ushort)),
]
assert sizeof(tagCAUI) == 8, sizeof(tagCAUI)
assert alignment(tagCAUI) == 4, alignment(tagCAUI)
class tagCAL(Structure):
    pass
tagCAL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_int)),
]
assert sizeof(tagCAL) == 8, sizeof(tagCAL)
assert alignment(tagCAL) == 4, alignment(tagCAL)
class tagCAUL(Structure):
    pass
tagCAUL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ulong)),
]
assert sizeof(tagCAUL) == 8, sizeof(tagCAUL)
assert alignment(tagCAUL) == 4, alignment(tagCAUL)
class tagCAH(Structure):
    pass
tagCAH._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_LARGE_INTEGER)),
]
assert sizeof(tagCAH) == 8, sizeof(tagCAH)
assert alignment(tagCAH) == 4, alignment(tagCAH)
class tagCAUH(Structure):
    pass
tagCAUH._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_ULARGE_INTEGER)),
]
assert sizeof(tagCAUH) == 8, sizeof(tagCAUH)
assert alignment(tagCAUH) == 4, alignment(tagCAUH)
class tagCAFLT(Structure):
    pass
tagCAFLT._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_float)),
]
assert sizeof(tagCAFLT) == 8, sizeof(tagCAFLT)
assert alignment(tagCAFLT) == 4, alignment(tagCAFLT)
class tagCADBL(Structure):
    pass
tagCADBL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_double)),
]
assert sizeof(tagCADBL) == 8, sizeof(tagCADBL)
assert alignment(tagCADBL) == 4, alignment(tagCADBL)
class tagCABOOL(Structure):
    pass
tagCABOOL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(VARIANT_BOOL)),
]
assert sizeof(tagCABOOL) == 8, sizeof(tagCABOOL)
assert alignment(tagCABOOL) == 4, alignment(tagCABOOL)
class tagCASCODE(Structure):
    pass
tagCASCODE._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(SCODE)),
]
assert sizeof(tagCASCODE) == 8, sizeof(tagCASCODE)
assert alignment(tagCASCODE) == 4, alignment(tagCASCODE)
class tagCACY(Structure):
    pass
tagCACY._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_longlong)),
]
assert sizeof(tagCACY) == 8, sizeof(tagCACY)
assert alignment(tagCACY) == 4, alignment(tagCACY)
class tagCADATE(Structure):
    pass
tagCADATE._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_double)),
]
assert sizeof(tagCADATE) == 8, sizeof(tagCADATE)
assert alignment(tagCADATE) == 4, alignment(tagCADATE)
class tagCAFILETIME(Structure):
    pass
tagCAFILETIME._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_FILETIME)),
]
assert sizeof(tagCAFILETIME) == 8, sizeof(tagCAFILETIME)
assert alignment(tagCAFILETIME) == 4, alignment(tagCAFILETIME)
class tagCACLSID(Structure):
    pass
tagCACLSID._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(GUID)),
]
assert sizeof(tagCACLSID) == 8, sizeof(tagCACLSID)
assert alignment(tagCACLSID) == 4, alignment(tagCACLSID)
class tagCACLIPDATA(Structure):
    pass
tagCACLIPDATA._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tagCLIPDATA)),
]
assert sizeof(tagCACLIPDATA) == 8, sizeof(tagCACLIPDATA)
assert alignment(tagCACLIPDATA) == 4, alignment(tagCACLIPDATA)
class tagCABSTR(Structure):
    pass
tagCABSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(BSTR)),
]
assert sizeof(tagCABSTR) == 8, sizeof(tagCABSTR)
assert alignment(tagCABSTR) == 4, alignment(tagCABSTR)
class tagCABSTRBLOB(Structure):
    pass
tagCABSTRBLOB._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tagBSTRBLOB)),
]
assert sizeof(tagCABSTRBLOB) == 8, sizeof(tagCABSTRBLOB)
assert alignment(tagCABSTRBLOB) == 4, alignment(tagCABSTRBLOB)
class tagCALPSTR(Structure):
    pass
tagCALPSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(STRING)),
]
assert sizeof(tagCALPSTR) == 8, sizeof(tagCALPSTR)
assert alignment(tagCALPSTR) == 4, alignment(tagCALPSTR)
class tagCALPWSTR(Structure):
    pass
tagCALPWSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(WSTRING)),
]
assert sizeof(tagCALPWSTR) == 8, sizeof(tagCALPWSTR)
assert alignment(tagCALPWSTR) == 4, alignment(tagCALPWSTR)
class tagCAPROPVARIANT(Structure):
    pass
tagCAPROPVARIANT._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tag_inner_PROPVARIANT)),
]
assert sizeof(tagCAPROPVARIANT) == 8, sizeof(tagCAPROPVARIANT)
assert alignment(tagCAPROPVARIANT) == 4, alignment(tagCAPROPVARIANT)
__MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001._fields_ = [
    ('cVal', c_char),
    ('bVal', c_ubyte),
    ('iVal', c_short),
    ('uiVal', c_ushort),
    ('lVal', c_int),
    ('ulVal', c_ulong),
    ('intVal', c_int),
    ('uintVal', c_uint),
    ('hVal', _LARGE_INTEGER),
    ('uhVal', _ULARGE_INTEGER),
    ('fltVal', c_float),
    ('dblVal', c_double),
    ('boolVal', VARIANT_BOOL),
    ('bool', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', c_longlong),
    ('date', c_double),
    ('filetime', _FILETIME),
    ('puuid', POINTER(GUID)),
    ('pClipData', POINTER(tagCLIPDATA)),
    ('bstrVal', BSTR),
    ('bstrblobVal', tagBSTRBLOB),
    ('blob', tagBLOB),
    ('pszVal', STRING),
    ('pwszVal', WSTRING),
    ('punkVal', POINTER(IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('pStream', POINTER(IStream)),
    ('pStorage', POINTER(IStorage)),
    ('pVersionedStream', POINTER(tagVersionedStream)),
    ('parray', wirePSAFEARRAY),
    ('cac', tagCAC),
    ('caub', tagCAUB),
    ('cai', tagCAI),
    ('caui', tagCAUI),
    ('cal', tagCAL),
    ('caul', tagCAUL),
    ('cah', tagCAH),
    ('cauh', tagCAUH),
    ('caflt', tagCAFLT),
    ('cadbl', tagCADBL),
    ('cabool', tagCABOOL),
    ('cascode', tagCASCODE),
    ('cacy', tagCACY),
    ('cadate', tagCADATE),
    ('cafiletime', tagCAFILETIME),
    ('cauuid', tagCACLSID),
    ('caclipdata', tagCACLIPDATA),
    ('cabstr', tagCABSTR),
    ('cabstrblob', tagCABSTRBLOB),
    ('calpstr', tagCALPSTR),
    ('calpwstr', tagCALPWSTR),
    ('capropvar', tagCAPROPVARIANT),
    ('pcVal', STRING),
    ('pbVal', POINTER(c_ubyte)),
    ('piVal', POINTER(c_short)),
    ('puiVal', POINTER(c_ushort)),
    ('plVal', POINTER(c_int)),
    ('pulVal', POINTER(c_ulong)),
    ('pintVal', POINTER(c_int)),
    ('puintVal', POINTER(c_uint)),
    ('pfltVal', POINTER(c_float)),
    ('pdblVal', POINTER(c_double)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pdecVal', POINTER(DECIMAL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(c_longlong)),
    ('pdate', POINTER(c_double)),
    ('pbstrVal', POINTER(BSTR)),
    ('ppunkVal', POINTER(POINTER(IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(wirePSAFEARRAY)),
    ('pvarVal', POINTER(tag_inner_PROPVARIANT)),
]
assert sizeof(__MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001) == 8, sizeof(__MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001)
assert alignment(__MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001) == 8, alignment(__MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001)
class IKnownFolder(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3AA7AF7E-9B36-420C-A8E3-F77D4674A488}')
    _idlflags_ = []

# values for enumeration 'FFFP_MODE'
FFFP_EXACTMATCH = 0
FFFP_NEARESTPARENTMATCH = 1
FFFP_MODE = c_int # enum
IKnownFolderManager._methods_ = [
    COMMETHOD([], HRESULT, 'FolderIdFromCsidl',
              ( ['in'], c_int, 'nCsidl' ),
              ( ['out'], POINTER(GUID), 'pfid' )),
    COMMETHOD([], HRESULT, 'FolderIdToCsidl',
              ( ['in'], POINTER(GUID), 'rfid' ),
              ( ['out'], POINTER(c_int), 'pnCsidl' )),
    COMMETHOD([], HRESULT, 'GetFolderIds',
              ( ['out'], POINTER(POINTER(GUID)), 'ppKFId' ),
              ( ['in', 'out'], POINTER(c_uint), 'pCount' )),
    COMMETHOD([], HRESULT, 'GetFolder',
              ( ['in'], POINTER(GUID), 'rfid' ),
              ( ['out'], POINTER(POINTER(IKnownFolder)), 'ppkf' )),
    COMMETHOD([], HRESULT, 'GetFolderByName',
              ( ['in'], WSTRING, 'pszCanonicalName' ),
              ( ['out'], POINTER(POINTER(IKnownFolder)), 'ppkf' )),
    COMMETHOD([], HRESULT, 'RegisterFolder',
              ( ['in'], POINTER(GUID), 'rfid' ),
              ( ['in'], POINTER(KNOWNFOLDER_DEFINITION), 'pKFD' )),
    COMMETHOD([], HRESULT, 'UnregisterFolder',
              ( ['in'], POINTER(GUID), 'rfid' )),
    COMMETHOD([], HRESULT, 'FindFolderFromPath',
              ( ['in'], WSTRING, 'pszPath' ),
              ( ['in'], FFFP_MODE, 'mode' ),
              ( ['out'], POINTER(POINTER(IKnownFolder)), 'ppkf' )),
    COMMETHOD([], HRESULT, 'FindFolderFromIDList',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['out'], POINTER(POINTER(IKnownFolder)), 'ppkf' )),
    COMMETHOD([], HRESULT, 'RemoteRedirect',
              ( ['in'], POINTER(GUID), 'rfid' ),
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_ulong, 'Flags' ),
              ( ['in'], WSTRING, 'pszTargetPath' ),
              ( ['in'], c_uint, 'cFolders' ),
              ( ['in'], POINTER(GUID), 'pExclusion' ),
              ( ['out'], POINTER(WSTRING), 'ppszError' )),
]
################################################################
## code template for IKnownFolderManager implementation
##class IKnownFolderManager_Impl(object):
##    def FolderIdFromCsidl(self, nCsidl):
##        '-no docstring-'
##        #return pfid
##
##    def FolderIdToCsidl(self, rfid):
##        '-no docstring-'
##        #return pnCsidl
##
##    def GetFolderIds(self):
##        '-no docstring-'
##        #return ppKFId, pCount
##
##    def GetFolder(self, rfid):
##        '-no docstring-'
##        #return ppkf
##
##    def GetFolderByName(self, pszCanonicalName):
##        '-no docstring-'
##        #return ppkf
##
##    def RegisterFolder(self, rfid, pKFD):
##        '-no docstring-'
##        #return
##
##    def UnregisterFolder(self, rfid):
##        '-no docstring-'
##        #return
##
##    def FindFolderFromPath(self, pszPath, mode):
##        '-no docstring-'
##        #return ppkf
##
##    def FindFolderFromIDList(self, pidl):
##        '-no docstring-'
##        #return ppkf
##
##    def RemoteRedirect(self, rfid, hwnd, Flags, pszTargetPath, cFolders, pExclusion):
##        '-no docstring-'
##        #return ppszError
##

IPersistStream._methods_ = [
    COMMETHOD([], HRESULT, 'IsDirty'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IStream), 'pstm' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], c_int, 'fClearDirty' )),
    COMMETHOD([], HRESULT, 'GetSizeMax',
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbSize' )),
]
################################################################
## code template for IPersistStream implementation
##class IPersistStream_Impl(object):
##    def IsDirty(self):
##        '-no docstring-'
##        #return
##
##    def Load(self, pstm):
##        '-no docstring-'
##        #return
##
##    def Save(self, pstm, fClearDirty):
##        '-no docstring-'
##        #return
##
##    def GetSizeMax(self):
##        '-no docstring-'
##        #return pcbSize
##


# values for enumeration 'GETPROPERTYSTOREFLAGS'
GPS_DEFAULT = 0
GPS_HANDLERPROPERTIESONLY = 1
GPS_READWRITE = 2
GPS_TEMPORARY = 4
GPS_FASTPROPERTIESONLY = 8
GPS_OPENSLOWITEM = 16
GPS_DELAYCREATION = 32
GPS_BESTEFFORT = 64
GPS_NO_OPLOCK = 128
GPS_PREFERQUERYPROPERTIES = 256
GPS_EXTRINSICPROPERTIES = 512
GPS_EXTRINSICPROPERTIESONLY = 1024
GPS_VOLATILEPROPERTIES = 2048
GPS_VOLATILEPROPERTIESONLY = 4096
GPS_MASK_VALID = 8191
GETPROPERTYSTOREFLAGS = c_int # enum

# values for enumeration 'TBPFLAG'
TBPF_NOPROGRESS = 0
TBPF_INDETERMINATE = 1
TBPF_NORMAL = 2
TBPF_ERROR = 4
TBPF_PAUSED = 8
TBPFLAG = c_int # enum
class _RemotableHandle(Structure):
    pass
wireHICON = POINTER(_RemotableHandle)
class IFrameworkInputPane(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5752238B-24F0-495A-82F1-2FD593056796}')
    _idlflags_ = []
class IFrameworkInputPaneHandler(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{226C537B-1E76-4D9E-A760-33DB29922F18}')
    _idlflags_ = []
IFrameworkInputPane._methods_ = [
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IUnknown), 'pWindow' ),
              ( ['in'], POINTER(IFrameworkInputPaneHandler), 'pHandler' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'AdviseWithHWND',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(IFrameworkInputPaneHandler), 'pHandler' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'Location',
              ( ['out'], POINTER(tagRECT), 'prcInputPaneScreenLocation' )),
]
################################################################
## code template for IFrameworkInputPane implementation
##class IFrameworkInputPane_Impl(object):
##    def Advise(self, pWindow, pHandler):
##        '-no docstring-'
##        #return pdwCookie
##
##    def AdviseWithHWND(self, hwnd, pHandler):
##        '-no docstring-'
##        #return pdwCookie
##
##    def Unadvise(self, dwCookie):
##        '-no docstring-'
##        #return
##
##    def Location(self):
##        '-no docstring-'
##        #return prcInputPaneScreenLocation
##

class IEnumMoniker(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000102-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IMoniker(IPersistStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000F-0000-0000-C000-000000000046}')
    _idlflags_ = []
IEnumMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum' )),
]
################################################################
## code template for IEnumMoniker implementation
##class IEnumMoniker_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class MailRecipient(CoClass):
    _reg_clsid_ = GUID('{9E56BE60-C50F-11CF-9A2C-00A0C90A90CE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
MailRecipient._com_interfaces_ = [IDropTarget]

class SharingConfigurationManager(CoClass):
    _reg_clsid_ = GUID('{49F371E1-8C5C-4D9C-9A3B-54A6827F513C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class ISharingConfigurationManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B4CD448A-9C86-4466-9201-2E62105B87AE}')
    _idlflags_ = []
SharingConfigurationManager._com_interfaces_ = [ISharingConfigurationManager]

class _userHMETAFILE(Structure):
    pass
_remoteMETAFILEPICT._fields_ = [
    ('mm', c_int),
    ('xExt', c_int),
    ('yExt', c_int),
    ('hMF', POINTER(_userHMETAFILE)),
]
assert sizeof(_remoteMETAFILEPICT) == 16, sizeof(_remoteMETAFILEPICT)
assert alignment(_remoteMETAFILEPICT) == 4, alignment(_remoteMETAFILEPICT)
class ICustomDestinationList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6332DEBF-87B5-4670-90C0-5E57B408A49E}')
    _idlflags_ = []
class IObjectArray(IUnknown):
    _case_insensitive_ = True
    'Unknown Object Array'
    _iid_ = GUID('{92CA9DCD-5622-4BBA-A805-5E9F541BD8C9}')
    _idlflags_ = []

# values for enumeration 'KNOWNDESTCATEGORY'
KDC_FREQUENT = 1
KDC_RECENT = 2
KNOWNDESTCATEGORY = c_int # enum
ICustomDestinationList._methods_ = [
    COMMETHOD([], HRESULT, 'SetAppID',
              ( ['in'], WSTRING, 'pszAppID' )),
    COMMETHOD([], HRESULT, 'BeginList',
              ( ['out'], POINTER(c_uint), 'pcMinSlots' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'AppendCategory',
              ( ['in'], WSTRING, 'pszCategory' ),
              ( ['in'], POINTER(IObjectArray), 'poa' )),
    COMMETHOD([], HRESULT, 'AppendKnownCategory',
              ( ['in'], KNOWNDESTCATEGORY, 'category' )),
    COMMETHOD([], HRESULT, 'AddUserTasks',
              ( ['in'], POINTER(IObjectArray), 'poa' )),
    COMMETHOD([], HRESULT, 'CommitList'),
    COMMETHOD([], HRESULT, 'GetRemovedDestinations',
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'DeleteList',
              ( ['in'], WSTRING, 'pszAppID' )),
    COMMETHOD([], HRESULT, 'AbortList'),
]
################################################################
## code template for ICustomDestinationList implementation
##class ICustomDestinationList_Impl(object):
##    def SetAppID(self, pszAppID):
##        '-no docstring-'
##        #return
##
##    def BeginList(self, riid):
##        '-no docstring-'
##        #return pcMinSlots, ppv
##
##    def AppendCategory(self, pszCategory, poa):
##        '-no docstring-'
##        #return
##
##    def AppendKnownCategory(self, category):
##        '-no docstring-'
##        #return
##
##    def AddUserTasks(self, poa):
##        '-no docstring-'
##        #return
##
##    def CommitList(self):
##        '-no docstring-'
##        #return
##
##    def GetRemovedDestinations(self, riid):
##        '-no docstring-'
##        #return ppv
##
##    def DeleteList(self, pszAppID):
##        '-no docstring-'
##        #return
##
##    def AbortList(self):
##        '-no docstring-'
##        #return
##

class IDefaultFolderMenuInitialize(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7690AA79-F8FC-4615-A327-36F7D18F5D91}')
    _idlflags_ = []
class IContextMenuCB(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3409E930-5A39-11D1-83FA-00A0C90DC849}')
    _idlflags_ = []
class IShellFolder(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{000214E6-0000-0000-C000-000000000046}')
    _idlflags_ = []

# values for enumeration 'DEFAULT_FOLDER_MENU_RESTRICTIONS'
DFMR_DEFAULT = 0
DFMR_NO_STATIC_VERBS = 8
DFMR_STATIC_VERBS_ONLY = 16
DFMR_NO_RESOURCE_VERBS = 32
DFMR_OPTIN_HANDLERS_ONLY = 64
DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY = 128
DFMR_USE_SPECIFIED_HANDLERS = 256
DFMR_USE_SPECIFIED_VERBS = 512
DFMR_NO_ASYNC_VERBS = 1024
DEFAULT_FOLDER_MENU_RESTRICTIONS = c_int # enum
IDefaultFolderMenuInitialize._methods_ = [
    COMMETHOD([], HRESULT, 'Initialize',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(IContextMenuCB), 'pcmcb' ),
              ( ['in'], wirePIDL, 'pidlFolder' ),
              ( ['in'], POINTER(IShellFolder), 'psf' ),
              ( ['in'], c_uint, 'cidl' ),
              ( ['in'], POINTER(wirePIDL), 'apidl' ),
              ( ['in'], POINTER(IUnknown), 'punkAssociation' ),
              ( ['in'], c_uint, 'cKeys' ),
              ( ['in'], POINTER(c_void_p), 'aKeys' )),
    COMMETHOD([], HRESULT, 'SetMenuRestrictions',
              ( ['in'], DEFAULT_FOLDER_MENU_RESTRICTIONS, 'dfmrValues' )),
    COMMETHOD([], HRESULT, 'GetMenuRestrictions',
              ( ['in'], DEFAULT_FOLDER_MENU_RESTRICTIONS, 'dfmrMask' ),
              ( ['out'], POINTER(DEFAULT_FOLDER_MENU_RESTRICTIONS), 'pdfmrValues' )),
    COMMETHOD([], HRESULT, 'SetHandlerClsid',
              ( ['in'], POINTER(GUID), 'rclsid' )),
]
################################################################
## code template for IDefaultFolderMenuInitialize implementation
##class IDefaultFolderMenuInitialize_Impl(object):
##    def Initialize(self, hwnd, pcmcb, pidlFolder, psf, cidl, apidl, punkAssociation, cKeys, aKeys):
##        '-no docstring-'
##        #return
##
##    def SetMenuRestrictions(self, dfmrValues):
##        '-no docstring-'
##        #return
##
##    def GetMenuRestrictions(self, dfmrMask):
##        '-no docstring-'
##        #return pdfmrValues
##
##    def SetHandlerClsid(self, rclsid):
##        '-no docstring-'
##        #return
##

class DriveSizeCategorizer(CoClass):
    _reg_clsid_ = GUID('{94357B53-CA29-4B78-83AE-E8FE7409134F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class ICategorizer(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A3B14589-9174-49A8-89A3-06A1AE2B9BA7}')
    _idlflags_ = []
DriveSizeCategorizer._com_interfaces_ = [ICategorizer]

class DestinationList(CoClass):
    _reg_clsid_ = GUID('{77F10CF0-3DB5-4966-B520-B7C54FD35ED6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
DestinationList._com_interfaces_ = [ICustomDestinationList]

class IBindCtx(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000E-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IRunningObjectTable(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000010-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumString(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000101-0000-0000-C000-000000000046}')
    _idlflags_ = []
IBindCtx._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'RevokeObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'ReleaseBoundObjects'),
    COMMETHOD([], HRESULT, 'RemoteSetBindOptions',
              ( ['in'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'RemoteGetBindOptions',
              ( ['in', 'out'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'GetRunningObjectTable',
              ( ['out'], POINTER(POINTER(IRunningObjectTable)), 'pprot' )),
    COMMETHOD([], HRESULT, 'RegisterObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'GetObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'EnumObjectParam',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'RevokeObjectParam',
              ( ['in'], WSTRING, 'pszKey' )),
]
################################################################
## code template for IBindCtx implementation
##class IBindCtx_Impl(object):
##    def RegisterObjectBound(self, punk):
##        '-no docstring-'
##        #return
##
##    def RevokeObjectBound(self, punk):
##        '-no docstring-'
##        #return
##
##    def ReleaseBoundObjects(self):
##        '-no docstring-'
##        #return
##
##    def RemoteSetBindOptions(self, pbindopts):
##        '-no docstring-'
##        #return
##
##    def RemoteGetBindOptions(self):
##        '-no docstring-'
##        #return pbindopts
##
##    def GetRunningObjectTable(self):
##        '-no docstring-'
##        #return pprot
##
##    def RegisterObjectParam(self, pszKey, punk):
##        '-no docstring-'
##        #return
##
##    def GetObjectParam(self, pszKey):
##        '-no docstring-'
##        #return ppunk
##
##    def EnumObjectParam(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RevokeObjectParam(self, pszKey):
##        '-no docstring-'
##        #return
##

class CATEGORY_INFO(Structure):
    pass

# values for enumeration 'CATSORT_FLAGS'
CATSORT_DEFAULT = 0
CATSORT_NAME = 1
CATSORT_FLAGS = c_int # enum
ICategorizer._methods_ = [
    COMMETHOD([], HRESULT, 'GetDescription',
              ( ['out'], WSTRING, 'pszDesc' ),
              ( ['in'], c_uint, 'cch' )),
    COMMETHOD([], HRESULT, 'GetCategory',
              ( ['in'], c_uint, 'cidl' ),
              ( ['in'], POINTER(wirePIDL), 'apidl' ),
              ( ['out'], POINTER(c_ulong), 'rgCategoryIds' )),
    COMMETHOD([], HRESULT, 'GetCategoryInfo',
              ( ['in'], c_ulong, 'dwCategoryId' ),
              ( ['out'], POINTER(CATEGORY_INFO), 'pci' )),
    COMMETHOD([], HRESULT, 'CompareCategory',
              ( ['in'], CATSORT_FLAGS, 'csfFlags' ),
              ( ['in'], c_ulong, 'dwCategoryId1' ),
              ( ['in'], c_ulong, 'dwCategoryId2' )),
]
################################################################
## code template for ICategorizer implementation
##class ICategorizer_Impl(object):
##    def GetDescription(self, cch):
##        '-no docstring-'
##        #return pszDesc
##
##    def GetCategory(self, cidl, apidl):
##        '-no docstring-'
##        #return rgCategoryIds
##
##    def GetCategoryInfo(self, dwCategoryId):
##        '-no docstring-'
##        #return pci
##
##    def CompareCategory(self, csfFlags, dwCategoryId1, dwCategoryId2):
##        '-no docstring-'
##        #return
##

class SizeCategorizer(CoClass):
    _reg_clsid_ = GUID('{55D7B852-F6D1-42F2-AA75-8728A1B2D264}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
SizeCategorizer._com_interfaces_ = [ICategorizer]

class DriveTypeCategorizer(CoClass):
    _reg_clsid_ = GUID('{B0A8F3CF-4333-4BAB-8873-1CCB1CADA48B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
DriveTypeCategorizer._com_interfaces_ = [ICategorizer]

class tagDVTARGETDEVICE(Structure):
    pass
tagDVTARGETDEVICE._fields_ = [
    ('tdSize', c_ulong),
    ('tdDriverNameOffset', c_ushort),
    ('tdDeviceNameOffset', c_ushort),
    ('tdPortNameOffset', c_ushort),
    ('tdExtDevmodeOffset', c_ushort),
    ('tdData', POINTER(c_ubyte)),
]
assert sizeof(tagDVTARGETDEVICE) == 16, sizeof(tagDVTARGETDEVICE)
assert alignment(tagDVTARGETDEVICE) == 4, alignment(tagDVTARGETDEVICE)
class _userHENHMETAFILE(Structure):
    pass
class __MIDL_IWinTypes_0006(Union):
    pass
__MIDL_IWinTypes_0006._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_BYTE_BLOB)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0006) == 8, sizeof(__MIDL_IWinTypes_0006)
assert alignment(__MIDL_IWinTypes_0006) == 8, alignment(__MIDL_IWinTypes_0006)
_userHENHMETAFILE._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0006),
]
assert sizeof(_userHENHMETAFILE) == 16, sizeof(_userHENHMETAFILE)
assert alignment(_userHENHMETAFILE) == 8, alignment(_userHENHMETAFILE)
class ApplicationDestinations(CoClass):
    _reg_clsid_ = GUID('{86C14003-4D6B-4EF3-A7B4-0506663B2E68}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IApplicationDestinations(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{12337D35-94C6-48A0-BCE7-6A9C69D4D600}')
    _idlflags_ = []
ApplicationDestinations._com_interfaces_ = [IApplicationDestinations]

IApplicationDestinations._methods_ = [
    COMMETHOD([], HRESULT, 'SetAppID',
              ( ['in'], WSTRING, 'pszAppID' )),
    COMMETHOD([], HRESULT, 'RemoveDestination',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'RemoveAllDestinations'),
]
################################################################
## code template for IApplicationDestinations implementation
##class IApplicationDestinations_Impl(object):
##    def SetAppID(self, pszAppID):
##        '-no docstring-'
##        #return
##
##    def RemoveDestination(self, punk):
##        '-no docstring-'
##        #return
##
##    def RemoveAllDestinations(self):
##        '-no docstring-'
##        #return
##


# values for enumeration 'tagCONDITION_TYPE'
CT_AND_CONDITION = 0
CT_OR_CONDITION = 1
CT_NOT_CONDITION = 2
CT_LEAF_CONDITION = 3
tagCONDITION_TYPE = c_int # enum

# values for enumeration 'tagCONDITION_OPERATION'
COP_IMPLICIT = 0
COP_EQUAL = 1
COP_NOTEQUAL = 2
COP_LESSTHAN = 3
COP_GREATERTHAN = 4
COP_LESSTHANOREQUAL = 5
COP_GREATERTHANOREQUAL = 6
COP_VALUE_STARTSWITH = 7
COP_VALUE_ENDSWITH = 8
COP_VALUE_CONTAINS = 9
COP_VALUE_NOTCONTAINS = 10
COP_DOSWILDCARDS = 11
COP_WORD_EQUAL = 12
COP_WORD_STARTSWITH = 13
COP_APPLICATION_SPECIFIC = 14
tagCONDITION_OPERATION = c_int # enum
class IRichChunk(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4FDEF69C-DBC9-454E-9910-B34F3C64B510}')
    _idlflags_ = []
ICondition._methods_ = [
    COMMETHOD([], HRESULT, 'GetConditionType',
              ( ['out', 'retval'], POINTER(tagCONDITION_TYPE), 'pNodeType' )),
    COMMETHOD([], HRESULT, 'GetSubConditions',
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out', 'retval'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'RemoteGetComparisonInfo',
              ( ['out'], POINTER(WSTRING), 'ppszPropertyName' ),
              ( ['out'], POINTER(tagCONDITION_OPERATION), 'pcop' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'ppropvar' )),
    COMMETHOD([], HRESULT, 'GetValueType',
              ( ['out', 'retval'], POINTER(WSTRING), 'ppszValueTypeName' )),
    COMMETHOD([], HRESULT, 'GetValueNormalization',
              ( ['out', 'retval'], POINTER(WSTRING), 'ppszNormalization' )),
    COMMETHOD([], HRESULT, 'RemoteGetInputTerms',
              ( ['out'], POINTER(POINTER(IRichChunk)), 'ppPropertyTerm' ),
              ( ['out'], POINTER(POINTER(IRichChunk)), 'ppOperationTerm' ),
              ( ['out'], POINTER(POINTER(IRichChunk)), 'ppValueTerm' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out', 'retval'], POINTER(POINTER(ICondition)), 'ppc' )),
]
################################################################
## code template for ICondition implementation
##class ICondition_Impl(object):
##    def GetConditionType(self):
##        '-no docstring-'
##        #return pNodeType
##
##    def GetSubConditions(self, riid):
##        '-no docstring-'
##        #return ppv
##
##    def RemoteGetComparisonInfo(self):
##        '-no docstring-'
##        #return ppszPropertyName, pcop, ppropvar
##
##    def GetValueType(self):
##        '-no docstring-'
##        #return ppszValueTypeName
##
##    def GetValueNormalization(self):
##        '-no docstring-'
##        #return ppszNormalization
##
##    def RemoteGetInputTerms(self):
##        '-no docstring-'
##        #return ppPropertyTerm, ppOperationTerm, ppValueTerm
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppc
##

tag_inner_PROPVARIANT._fields_ = [
    ('vt', c_ushort),
    ('wReserved1', c_ubyte),
    ('wReserved2', c_ubyte),
    ('wReserved3', c_ulong),
    ('__MIDL____MIDL_itf_ShObjIdl_core_0003_00880001', __MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001),
]
assert sizeof(tag_inner_PROPVARIANT) == 16, sizeof(tag_inner_PROPVARIANT)
assert alignment(tag_inner_PROPVARIANT) == 8, alignment(tag_inner_PROPVARIANT)
class DesktopWallpaper(CoClass):
    _reg_clsid_ = GUID('{C2CF3110-460E-4FC1-B9D0-8A1C0C9CC4BD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IDesktopWallpaper(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}')
    _idlflags_ = []
DesktopWallpaper._com_interfaces_ = [IDesktopWallpaper]

class NetworkExplorerFolder(CoClass):
    _reg_clsid_ = GUID('{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IShellFolder2(IShellFolder):
    _case_insensitive_ = True
    _iid_ = GUID('{93F2F68C-1D1B-11D3-A30E-00C04F79ABD1}')
    _idlflags_ = []
NetworkExplorerFolder._com_interfaces_ = [IShellFolder2]

class THUMBBUTTON(Structure):
    pass

# values for enumeration 'THUMBBUTTONMASK'
THB_BITMAP = 1
THB_ICON = 2
THB_TOOLTIP = 4
THB_FLAGS = 8
THUMBBUTTONMASK = c_int # enum

# values for enumeration 'THUMBBUTTONFLAGS'
THBF_ENABLED = 0
THBF_DISABLED = 1
THBF_DISMISSONCLICK = 2
THBF_NOBACKGROUND = 4
THBF_HIDDEN = 8
THBF_NONINTERACTIVE = 16
THUMBBUTTONFLAGS = c_int # enum
THUMBBUTTON._fields_ = [
    ('dwMask', THUMBBUTTONMASK),
    ('iid', c_uint),
    ('iBitmap', c_uint),
    ('hIcon', wireHICON),
    ('szTip', c_ushort * 260),
    ('dwFlags', THUMBBUTTONFLAGS),
]
assert sizeof(THUMBBUTTON) == 540, sizeof(THUMBBUTTON)
assert alignment(THUMBBUTTON) == 4, alignment(THUMBBUTTON)
_FLAGGED_WORD_BLOB._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('asData', POINTER(c_ushort)),
]
assert sizeof(_FLAGGED_WORD_BLOB) == 12, sizeof(_FLAGGED_WORD_BLOB)
assert alignment(_FLAGGED_WORD_BLOB) == 4, alignment(_FLAGGED_WORD_BLOB)

# values for enumeration 'APPLICATION_VIEW_ORIENTATION'
AVO_LANDSCAPE = 0
AVO_PORTRAIT = 1
APPLICATION_VIEW_ORIENTATION = c_int # enum
class __MIDL_IWinTypes_0004(Union):
    pass
__MIDL_IWinTypes_0004._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_BYTE_BLOB)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0004) == 8, sizeof(__MIDL_IWinTypes_0004)
assert alignment(__MIDL_IWinTypes_0004) == 8, alignment(__MIDL_IWinTypes_0004)
_userHMETAFILE._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0004),
]
assert sizeof(_userHMETAFILE) == 16, sizeof(_userHMETAFILE)
assert alignment(_userHMETAFILE) == 8, alignment(_userHMETAFILE)

# values for enumeration 'ADJACENT_DISPLAY_EDGES'
ADE_NONE = 0
ADE_LEFT = 1
ADE_RIGHT = 2
ADJACENT_DISPLAY_EDGES = c_int # enum
class IAppVisibility(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2246EA2D-CAEA-4444-A3C4-6DE827E44313}')
    _idlflags_ = []
wireHMONITOR = POINTER(_RemotableHandle)

# values for enumeration 'MONITOR_APP_VISIBILITY'
MAV_UNKNOWN = 0
MAV_NO_APP_VISIBLE = 1
MAV_APP_VISIBLE = 2
MONITOR_APP_VISIBILITY = c_int # enum
class IAppVisibilityEvents(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6584CE6B-7D82-49C2-89C9-C6BC02BA8C38}')
    _idlflags_ = []
IAppVisibility._methods_ = [
    COMMETHOD([], HRESULT, 'GetAppVisibilityOnMonitor',
              ( ['in'], wireHMONITOR, 'hMonitor' ),
              ( ['out'], POINTER(MONITOR_APP_VISIBILITY), 'pMode' )),
    COMMETHOD([], HRESULT, 'IsLauncherVisible',
              ( ['out'], POINTER(c_int), 'pfVisible' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IAppVisibilityEvents), 'pCallback' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
]
################################################################
## code template for IAppVisibility implementation
##class IAppVisibility_Impl(object):
##    def GetAppVisibilityOnMonitor(self, hMonitor):
##        '-no docstring-'
##        #return pMode
##
##    def IsLauncherVisible(self):
##        '-no docstring-'
##        #return pfVisible
##
##    def Advise(self, pCallback):
##        '-no docstring-'
##        #return pdwCookie
##
##    def Unadvise(self, dwCookie):
##        '-no docstring-'
##        #return
##

_tagpropertykey._fields_ = [
    ('fmtid', GUID),
    ('pid', c_ulong),
]
assert sizeof(_tagpropertykey) == 20, sizeof(_tagpropertykey)
assert alignment(_tagpropertykey) == 4, alignment(_tagpropertykey)
SORTCOLUMN._fields_ = [
    ('propkey', _tagpropertykey),
    ('direction', c_int),
]
assert sizeof(SORTCOLUMN) == 24, sizeof(SORTCOLUMN)
assert alignment(SORTCOLUMN) == 4, alignment(SORTCOLUMN)
class Library(object):
    name = 'ShellCoreObjects'
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)

class tagFORMATETC(Structure):
    pass
class _userSTGMEDIUM(Structure):
    pass
wireSTGMEDIUM = POINTER(_userSTGMEDIUM)
class _userFLAG_STGMEDIUM(Structure):
    pass
wireFLAG_STGMEDIUM = POINTER(_userFLAG_STGMEDIUM)
class IEnumFORMATETC(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000103-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IAdviseSink(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000010F-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumSTATDATA(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000105-0000-0000-C000-000000000046}')
    _idlflags_ = []
IDataObject._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteGetData',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetcIn' ),
              ( ['out'], POINTER(wireSTGMEDIUM), 'pRemoteMedium' )),
    COMMETHOD([], HRESULT, 'RemoteGetDataHere',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in', 'out'], POINTER(wireSTGMEDIUM), 'pRemoteMedium' )),
    COMMETHOD([], HRESULT, 'QueryGetData',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' )),
    COMMETHOD([], HRESULT, 'GetCanonicalFormatEtc',
              ( ['in'], POINTER(tagFORMATETC), 'pformatectIn' ),
              ( ['out'], POINTER(tagFORMATETC), 'pformatetcOut' )),
    COMMETHOD([], HRESULT, 'RemoteSetData',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in'], POINTER(wireFLAG_STGMEDIUM), 'pmedium' ),
              ( ['in'], c_int, 'fRelease' )),
    COMMETHOD([], HRESULT, 'EnumFormatEtc',
              ( ['in'], c_ulong, 'dwDirection' ),
              ( ['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenumFormatEtc' )),
    COMMETHOD([], HRESULT, 'DAdvise',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in'], c_ulong, 'advf' ),
              ( ['in'], POINTER(IAdviseSink), 'pAdvSink' ),
              ( ['out'], POINTER(c_ulong), 'pdwConnection' )),
    COMMETHOD([], HRESULT, 'DUnadvise',
              ( ['in'], c_ulong, 'dwConnection' )),
    COMMETHOD([], HRESULT, 'EnumDAdvise',
              ( ['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenumAdvise' )),
]
################################################################
## code template for IDataObject implementation
##class IDataObject_Impl(object):
##    def RemoteGetData(self, pformatetcIn):
##        '-no docstring-'
##        #return pRemoteMedium
##
##    def RemoteGetDataHere(self, pformatetc):
##        '-no docstring-'
##        #return pRemoteMedium
##
##    def QueryGetData(self, pformatetc):
##        '-no docstring-'
##        #return
##
##    def GetCanonicalFormatEtc(self, pformatectIn):
##        '-no docstring-'
##        #return pformatetcOut
##
##    def RemoteSetData(self, pformatetc, pmedium, fRelease):
##        '-no docstring-'
##        #return
##
##    def EnumFormatEtc(self, dwDirection):
##        '-no docstring-'
##        #return ppenumFormatEtc
##
##    def DAdvise(self, pformatetc, advf, pAdvSink):
##        '-no docstring-'
##        #return pdwConnection
##
##    def DUnadvise(self, dwConnection):
##        '-no docstring-'
##        #return
##
##    def EnumDAdvise(self):
##        '-no docstring-'
##        #return ppenumAdvise
##

class IModalWindow(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B4DB1657-70D7-485E-8E3E-6FCB5A5C1802}')
    _idlflags_ = []
IModalWindow._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteShow',
              ( ['in'], wireHWND, 'hwndOwner' )),
]
################################################################
## code template for IModalWindow implementation
##class IModalWindow_Impl(object):
##    def RemoteShow(self, hwndOwner):
##        '-no docstring-'
##        #return
##

class NetworkConnections(CoClass):
    _reg_clsid_ = GUID('{7007ACC7-3202-11D1-AAD2-00805FC1270E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
NetworkConnections._com_interfaces_ = [IShellFolder2]


# values for enumeration 'DEF_SHARE_ID'
DEFSHAREID_USERS = 1
DEFSHAREID_PUBLIC = 2
DEF_SHARE_ID = c_int # enum

# values for enumeration 'SHARE_ROLE'
SHARE_ROLE_INVALID = -1
SHARE_ROLE_READER = 0
SHARE_ROLE_CONTRIBUTOR = 1
SHARE_ROLE_CO_OWNER = 2
SHARE_ROLE_OWNER = 3
SHARE_ROLE_CUSTOM = 4
SHARE_ROLE_MIXED = 5
SHARE_ROLE = c_int # enum
ISharingConfigurationManager._methods_ = [
    COMMETHOD([], HRESULT, 'CreateShare',
              ( ['in'], DEF_SHARE_ID, 'dsid' ),
              ( ['in'], SHARE_ROLE, 'role' )),
    COMMETHOD([], HRESULT, 'DeleteShare',
              ( ['in'], DEF_SHARE_ID, 'dsid' )),
    COMMETHOD([], HRESULT, 'ShareExists',
              ( ['in'], DEF_SHARE_ID, 'dsid' )),
    COMMETHOD([], HRESULT, 'GetSharePermissions',
              ( ['in'], DEF_SHARE_ID, 'dsid' ),
              ( ['out'], POINTER(SHARE_ROLE), 'pRole' )),
    COMMETHOD([], HRESULT, 'SharePrinters'),
    COMMETHOD([], HRESULT, 'StopSharingPrinters'),
    COMMETHOD([], HRESULT, 'ArePrintersShared'),
]
################################################################
## code template for ISharingConfigurationManager implementation
##class ISharingConfigurationManager_Impl(object):
##    def CreateShare(self, dsid, role):
##        '-no docstring-'
##        #return
##
##    def DeleteShare(self, dsid):
##        '-no docstring-'
##        #return
##
##    def ShareExists(self, dsid):
##        '-no docstring-'
##        #return
##
##    def GetSharePermissions(self, dsid):
##        '-no docstring-'
##        #return pRole
##
##    def SharePrinters(self):
##        '-no docstring-'
##        #return
##
##    def StopSharingPrinters(self):
##        '-no docstring-'
##        #return
##
##    def ArePrintersShared(self):
##        '-no docstring-'
##        #return
##

class __MIDL_IWinTypes_0007(Union):
    pass
class _userBITMAP(Structure):
    pass
__MIDL_IWinTypes_0007._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_userBITMAP)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0007) == 8, sizeof(__MIDL_IWinTypes_0007)
assert alignment(__MIDL_IWinTypes_0007) == 8, alignment(__MIDL_IWinTypes_0007)
class IUserNotification(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BA9711BA-5893-4787-A7E1-41277151550B}')
    _idlflags_ = []
class IQueryContinue(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7307055C-B24A-486B-9F25-163E597A28A9}')
    _idlflags_ = []
IUserNotification._methods_ = [
    COMMETHOD([], HRESULT, 'SetBalloonInfo',
              ( ['in'], WSTRING, 'pszTitle' ),
              ( ['in'], WSTRING, 'pszText' ),
              ( ['in'], c_ulong, 'dwInfoFlags' )),
    COMMETHOD([], HRESULT, 'SetBalloonRetry',
              ( ['in'], c_ulong, 'dwShowTime' ),
              ( ['in'], c_ulong, 'dwInterval' ),
              ( ['in'], c_uint, 'cRetryCount' )),
    COMMETHOD([], HRESULT, 'SetIconInfo',
              ( ['in'], wireHICON, 'hIcon' ),
              ( ['in'], WSTRING, 'pszToolTip' )),
    COMMETHOD([], HRESULT, 'Show',
              ( ['in'], POINTER(IQueryContinue), 'pqc' ),
              ( ['in'], c_ulong, 'dwContinuePollInterval' )),
    COMMETHOD([], HRESULT, 'PlaySound',
              ( ['in'], WSTRING, 'pszSoundName' )),
]
################################################################
## code template for IUserNotification implementation
##class IUserNotification_Impl(object):
##    def SetBalloonInfo(self, pszTitle, pszText, dwInfoFlags):
##        '-no docstring-'
##        #return
##
##    def SetBalloonRetry(self, dwShowTime, dwInterval, cRetryCount):
##        '-no docstring-'
##        #return
##
##    def SetIconInfo(self, hIcon, pszToolTip):
##        '-no docstring-'
##        #return
##
##    def Show(self, pqc, dwContinuePollInterval):
##        '-no docstring-'
##        #return
##
##    def PlaySound(self, pszSoundName):
##        '-no docstring-'
##        #return
##

class IFileDialog(IModalWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{42F85136-DB7E-439C-85F1-E4075D135FC8}')
    _idlflags_ = []
class IFileOpenDialog(IFileDialog):
    _case_insensitive_ = True
    _iid_ = GUID('{D57C7288-D4AD-4768-BE02-9D969532D960}')
    _idlflags_ = []
class _COMDLG_FILTERSPEC(Structure):
    pass
class IFileDialogEvents(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{973510DB-7D7F-452B-8975-74A85828D354}')
    _idlflags_ = []
class IShellItem(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{43826D1E-E718-42EE-BC55-A1E261C37BFE}')
    _idlflags_ = []

# values for enumeration 'FDAP'
FDAP_BOTTOM = 0
FDAP_TOP = 1
FDAP = c_int # enum
class IShellItemFilter(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2659B475-EEB8-48B7-8F07-B378810F48CF}')
    _idlflags_ = []
IFileDialog._methods_ = [
    COMMETHOD([], HRESULT, 'SetFileTypes',
              ( ['in'], c_uint, 'cFileTypes' ),
              ( ['in'], POINTER(_COMDLG_FILTERSPEC), 'rgFilterSpec' )),
    COMMETHOD([], HRESULT, 'SetFileTypeIndex',
              ( ['in'], c_uint, 'iFileType' )),
    COMMETHOD([], HRESULT, 'GetFileTypeIndex',
              ( ['out'], POINTER(c_uint), 'piFileType' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IFileDialogEvents), 'pfde' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'SetOptions',
              ( ['in'], c_ulong, 'fos' )),
    COMMETHOD([], HRESULT, 'GetOptions',
              ( ['out'], POINTER(c_ulong), 'pfos' )),
    COMMETHOD([], HRESULT, 'SetDefaultFolder',
              ( ['in'], POINTER(IShellItem), 'psi' )),
    COMMETHOD([], HRESULT, 'SetFolder',
              ( ['in'], POINTER(IShellItem), 'psi' )),
    COMMETHOD([], HRESULT, 'GetFolder',
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsi' )),
    COMMETHOD([], HRESULT, 'GetCurrentSelection',
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsi' )),
    COMMETHOD([], HRESULT, 'SetFileName',
              ( ['in'], WSTRING, 'pszName' )),
    COMMETHOD([], HRESULT, 'GetFileName',
              ( ['out'], POINTER(WSTRING), 'pszName' )),
    COMMETHOD([], HRESULT, 'SetTitle',
              ( ['in'], WSTRING, 'pszTitle' )),
    COMMETHOD([], HRESULT, 'SetOkButtonLabel',
              ( ['in'], WSTRING, 'pszText' )),
    COMMETHOD([], HRESULT, 'SetFileNameLabel',
              ( ['in'], WSTRING, 'pszLabel' )),
    COMMETHOD([], HRESULT, 'GetResult',
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsi' )),
    COMMETHOD([], HRESULT, 'AddPlace',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], FDAP, 'FDAP' )),
    COMMETHOD([], HRESULT, 'SetDefaultExtension',
              ( ['in'], WSTRING, 'pszDefaultExtension' )),
    COMMETHOD([], HRESULT, 'Close',
              ( ['in'], HRESULT, 'hr' )),
    COMMETHOD([], HRESULT, 'SetClientGuid',
              ( ['in'], POINTER(GUID), 'guid' )),
    COMMETHOD([], HRESULT, 'ClearClientData'),
    COMMETHOD([], HRESULT, 'SetFilter',
              ( ['in'], POINTER(IShellItemFilter), 'pFilter' )),
]
################################################################
## code template for IFileDialog implementation
##class IFileDialog_Impl(object):
##    def SetFileTypes(self, cFileTypes, rgFilterSpec):
##        '-no docstring-'
##        #return
##
##    def SetFileTypeIndex(self, iFileType):
##        '-no docstring-'
##        #return
##
##    def GetFileTypeIndex(self):
##        '-no docstring-'
##        #return piFileType
##
##    def Advise(self, pfde):
##        '-no docstring-'
##        #return pdwCookie
##
##    def Unadvise(self, dwCookie):
##        '-no docstring-'
##        #return
##
##    def SetOptions(self, fos):
##        '-no docstring-'
##        #return
##
##    def GetOptions(self):
##        '-no docstring-'
##        #return pfos
##
##    def SetDefaultFolder(self, psi):
##        '-no docstring-'
##        #return
##
##    def SetFolder(self, psi):
##        '-no docstring-'
##        #return
##
##    def GetFolder(self):
##        '-no docstring-'
##        #return ppsi
##
##    def GetCurrentSelection(self):
##        '-no docstring-'
##        #return ppsi
##
##    def SetFileName(self, pszName):
##        '-no docstring-'
##        #return
##
##    def GetFileName(self):
##        '-no docstring-'
##        #return pszName
##
##    def SetTitle(self, pszTitle):
##        '-no docstring-'
##        #return
##
##    def SetOkButtonLabel(self, pszText):
##        '-no docstring-'
##        #return
##
##    def SetFileNameLabel(self, pszLabel):
##        '-no docstring-'
##        #return
##
##    def GetResult(self):
##        '-no docstring-'
##        #return ppsi
##
##    def AddPlace(self, psi, FDAP):
##        '-no docstring-'
##        #return
##
##    def SetDefaultExtension(self, pszDefaultExtension):
##        '-no docstring-'
##        #return
##
##    def Close(self, hr):
##        '-no docstring-'
##        #return
##
##    def SetClientGuid(self, guid):
##        '-no docstring-'
##        #return
##
##    def ClearClientData(self):
##        '-no docstring-'
##        #return
##
##    def SetFilter(self, pFilter):
##        '-no docstring-'
##        #return
##

IFileOpenDialog._methods_ = [
    COMMETHOD([], HRESULT, 'GetResults',
              ( ['out'], POINTER(POINTER(IShellItemArray)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetSelectedItems',
              ( ['out'], POINTER(POINTER(IShellItemArray)), 'ppsai' )),
]
################################################################
## code template for IFileOpenDialog implementation
##class IFileOpenDialog_Impl(object):
##    def GetResults(self):
##        '-no docstring-'
##        #return ppenum
##
##    def GetSelectedItems(self):
##        '-no docstring-'
##        #return ppsai
##

class _GDI_OBJECT(Structure):
    pass
class __MIDL_IAdviseSink_0002(Union):
    pass
class _userHBITMAP(Structure):
    pass
class _userHPALETTE(Structure):
    pass
class _userHGLOBAL(Structure):
    pass
__MIDL_IAdviseSink_0002._fields_ = [
    ('hBitmap', POINTER(_userHBITMAP)),
    ('hPalette', POINTER(_userHPALETTE)),
    ('hGeneric', POINTER(_userHGLOBAL)),
]
assert sizeof(__MIDL_IAdviseSink_0002) == 4, sizeof(__MIDL_IAdviseSink_0002)
assert alignment(__MIDL_IAdviseSink_0002) == 4, alignment(__MIDL_IAdviseSink_0002)
_GDI_OBJECT._fields_ = [
    ('ObjectType', c_ulong),
    ('u', __MIDL_IAdviseSink_0002),
]
assert sizeof(_GDI_OBJECT) == 8, sizeof(_GDI_OBJECT)
assert alignment(_GDI_OBJECT) == 4, alignment(_GDI_OBJECT)

# values for enumeration 'DESKTOP_WALLPAPER_POSITION'
DWPOS_CENTER = 0
DWPOS_TILE = 1
DWPOS_STRETCH = 2
DWPOS_FIT = 3
DWPOS_FILL = 4
DWPOS_SPAN = 5
DESKTOP_WALLPAPER_POSITION = c_int # enum

# values for enumeration 'DESKTOP_SLIDESHOW_OPTIONS'
DSO_SHUFFLEIMAGES = 1
DESKTOP_SLIDESHOW_OPTIONS = c_int # enum

# values for enumeration 'DESKTOP_SLIDESHOW_DIRECTION'
DSD_FORWARD = 0
DSD_BACKWARD = 1
DESKTOP_SLIDESHOW_DIRECTION = c_int # enum

# values for enumeration 'DESKTOP_SLIDESHOW_STATE'
DSS_ENABLED = 1
DSS_SLIDESHOW = 2
DSS_DISABLED_BY_REMOTE_SESSION = 4
DESKTOP_SLIDESHOW_STATE = c_int # enum
IDesktopWallpaper._methods_ = [
    COMMETHOD([], HRESULT, 'SetWallpaper',
              ( ['in'], WSTRING, 'monitorID' ),
              ( ['in'], WSTRING, 'wallpaper' )),
    COMMETHOD([], HRESULT, 'GetWallpaper',
              ( ['in'], WSTRING, 'monitorID' ),
              ( ['out'], POINTER(WSTRING), 'wallpaper' )),
    COMMETHOD([], HRESULT, 'GetMonitorDevicePathAt',
              ( ['in'], c_uint, 'monitorIndex' ),
              ( ['out'], POINTER(WSTRING), 'monitorID' )),
    COMMETHOD([], HRESULT, 'GetMonitorDevicePathCount',
              ( ['out'], POINTER(c_uint), 'count' )),
    COMMETHOD([], HRESULT, 'GetMonitorRECT',
              ( ['in'], WSTRING, 'monitorID' ),
              ( ['out'], POINTER(tagRECT), 'displayRect' )),
    COMMETHOD([], HRESULT, 'SetBackgroundColor',
              ( ['in'], c_ulong, 'color' )),
    COMMETHOD([], HRESULT, 'GetBackgroundColor',
              ( ['out'], POINTER(c_ulong), 'color' )),
    COMMETHOD([], HRESULT, 'SetPosition',
              ( ['in'], DESKTOP_WALLPAPER_POSITION, 'position' )),
    COMMETHOD([], HRESULT, 'GetPosition',
              ( ['out'], POINTER(DESKTOP_WALLPAPER_POSITION), 'position' )),
    COMMETHOD([], HRESULT, 'SetSlideshow',
              ( ['in'], POINTER(IShellItemArray), 'items' )),
    COMMETHOD([], HRESULT, 'GetSlideshow',
              ( ['out'], POINTER(POINTER(IShellItemArray)), 'items' )),
    COMMETHOD([], HRESULT, 'SetSlideshowOptions',
              ( ['in'], DESKTOP_SLIDESHOW_OPTIONS, 'options' ),
              ( ['in'], c_uint, 'slideshowTick' )),
    COMMETHOD([], HRESULT, 'GetSlideshowOptions',
              ( ['out'], POINTER(DESKTOP_SLIDESHOW_OPTIONS), 'options' ),
              ( ['out'], POINTER(c_uint), 'slideshowTick' )),
    COMMETHOD([], HRESULT, 'AdvanceSlideshow',
              ( ['in'], WSTRING, 'monitorID' ),
              ( ['in'], DESKTOP_SLIDESHOW_DIRECTION, 'direction' )),
    COMMETHOD([], HRESULT, 'GetStatus',
              ( ['out'], POINTER(DESKTOP_SLIDESHOW_STATE), 'state' )),
    COMMETHOD([], HRESULT, 'Enable',
              ( ['in'], c_int, 'Enable' )),
]
################################################################
## code template for IDesktopWallpaper implementation
##class IDesktopWallpaper_Impl(object):
##    def SetWallpaper(self, monitorID, wallpaper):
##        '-no docstring-'
##        #return
##
##    def GetWallpaper(self, monitorID):
##        '-no docstring-'
##        #return wallpaper
##
##    def GetMonitorDevicePathAt(self, monitorIndex):
##        '-no docstring-'
##        #return monitorID
##
##    def GetMonitorDevicePathCount(self):
##        '-no docstring-'
##        #return count
##
##    def GetMonitorRECT(self, monitorID):
##        '-no docstring-'
##        #return displayRect
##
##    def SetBackgroundColor(self, color):
##        '-no docstring-'
##        #return
##
##    def GetBackgroundColor(self):
##        '-no docstring-'
##        #return color
##
##    def SetPosition(self, position):
##        '-no docstring-'
##        #return
##
##    def GetPosition(self):
##        '-no docstring-'
##        #return position
##
##    def SetSlideshow(self, items):
##        '-no docstring-'
##        #return
##
##    def GetSlideshow(self):
##        '-no docstring-'
##        #return items
##
##    def SetSlideshowOptions(self, options, slideshowTick):
##        '-no docstring-'
##        #return
##
##    def GetSlideshowOptions(self):
##        '-no docstring-'
##        #return options, slideshowTick
##
##    def AdvanceSlideshow(self, monitorID, direction):
##        '-no docstring-'
##        #return
##
##    def GetStatus(self):
##        '-no docstring-'
##        #return state
##
##    def Enable(self, Enable):
##        '-no docstring-'
##        #return
##

class FileOpenDialog(CoClass):
    _reg_clsid_ = GUID('{DC1C5A9C-E88A-4DDE-A5A1-60F82A20AEF7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
FileOpenDialog._com_interfaces_ = [IFileOpenDialog]


# values for enumeration 'CATEGORYINFO_FLAGS'
CATINFO_NORMAL = 0
CATINFO_COLLAPSED = 1
CATINFO_HIDDEN = 2
CATINFO_EXPANDED = 4
CATINFO_NOHEADER = 8
CATINFO_NOTCOLLAPSIBLE = 16
CATINFO_NOHEADERCOUNT = 32
CATINFO_SUBSETTED = 64
CATINFO_SEPARATE_IMAGES = 128
CATINFO_SHOWEMPTY = 256
CATEGORYINFO_FLAGS = c_int # enum
CATEGORY_INFO._fields_ = [
    ('cif', CATEGORYINFO_FLAGS),
    ('wszName', c_ushort * 260),
]
assert sizeof(CATEGORY_INFO) == 524, sizeof(CATEGORY_INFO)
assert alignment(CATEGORY_INFO) == 4, alignment(CATEGORY_INFO)
class _userCLIPFORMAT(Structure):
    pass
wireCLIPFORMAT = POINTER(_userCLIPFORMAT)
tagFORMATETC._fields_ = [
    ('cfFormat', wireCLIPFORMAT),
    ('ptd', POINTER(tagDVTARGETDEVICE)),
    ('dwAspect', c_ulong),
    ('lindex', c_int),
    ('tymed', c_ulong),
]
assert sizeof(tagFORMATETC) == 20, sizeof(tagFORMATETC)
assert alignment(tagFORMATETC) == 4, alignment(tagFORMATETC)
IObjectArray._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_uint), 'pcObjects' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_uint, 'uiIndex' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
]
################################################################
## code template for IObjectArray implementation
##class IObjectArray_Impl(object):
##    def GetCount(self):
##        '-no docstring-'
##        #return pcObjects
##
##    def GetAt(self, uiIndex, riid):
##        '-no docstring-'
##        #return ppv
##

IEnumString._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(WSTRING), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
]
################################################################
## code template for IEnumString implementation
##class IEnumString_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class tagSTATSTG(Structure):
    pass
tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
assert sizeof(tagSTATSTG) == 72, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
IKnownFolder._methods_ = [
    COMMETHOD([], HRESULT, 'GetId',
              ( ['out'], POINTER(GUID), 'pkfid' )),
    COMMETHOD([], HRESULT, 'GetCategory',
              ( ['out'], POINTER(KF_CATEGORY), 'pCategory' )),
    COMMETHOD([], HRESULT, 'GetShellItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetPath',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['out'], POINTER(WSTRING), 'ppszPath' )),
    COMMETHOD([], HRESULT, 'SetPath',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], WSTRING, 'pszPath' )),
    COMMETHOD([], HRESULT, 'GetIDList',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['out'], POINTER(wirePIDL), 'ppidl' )),
    COMMETHOD([], HRESULT, 'GetFolderType',
              ( ['out'], POINTER(GUID), 'pftid' )),
    COMMETHOD([], HRESULT, 'GetRedirectionCapabilities',
              ( ['out'], POINTER(c_ulong), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'GetFolderDefinition',
              ( ['out'], POINTER(KNOWNFOLDER_DEFINITION), 'pKFD' )),
]
################################################################
## code template for IKnownFolder implementation
##class IKnownFolder_Impl(object):
##    def GetId(self):
##        '-no docstring-'
##        #return pkfid
##
##    def GetCategory(self):
##        '-no docstring-'
##        #return pCategory
##
##    def GetShellItem(self, dwFlags, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetPath(self, dwFlags):
##        '-no docstring-'
##        #return ppszPath
##
##    def SetPath(self, dwFlags, pszPath):
##        '-no docstring-'
##        #return
##
##    def GetIDList(self, dwFlags):
##        '-no docstring-'
##        #return ppidl
##
##    def GetFolderType(self):
##        '-no docstring-'
##        #return pftid
##
##    def GetRedirectionCapabilities(self):
##        '-no docstring-'
##        #return pCapabilities
##
##    def GetFolderDefinition(self):
##        '-no docstring-'
##        #return pKFD
##

class ApplicationDocumentLists(CoClass):
    _reg_clsid_ = GUID('{86BEC222-30F2-47E0-9F25-60D11CD75C28}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IApplicationDocumentLists(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3C594F9F-9F30-47A1-979A-C9E83D3D0A06}')
    _idlflags_ = []
ApplicationDocumentLists._com_interfaces_ = [IApplicationDocumentLists]

class __MIDL_IWinTypes_0001(Union):
    pass
__MIDL_IWinTypes_0001._fields_ = [
    ('dwValue', c_ulong),
    ('pwszName', WSTRING),
]
assert sizeof(__MIDL_IWinTypes_0001) == 4, sizeof(__MIDL_IWinTypes_0001)
assert alignment(__MIDL_IWinTypes_0001) == 4, alignment(__MIDL_IWinTypes_0001)
_userCLIPFORMAT._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0001),
]
assert sizeof(_userCLIPFORMAT) == 8, sizeof(_userCLIPFORMAT)
assert alignment(_userCLIPFORMAT) == 4, alignment(_userCLIPFORMAT)
class __MIDL_IOleAutomationTypes_0004(Union):
    pass
__MIDL_IOleAutomationTypes_0004._fields_ = [
    ('llVal', c_longlong),
    ('lVal', c_int),
    ('bVal', c_ubyte),
    ('iVal', c_short),
    ('fltVal', c_float),
    ('dblVal', c_double),
    ('boolVal', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', c_longlong),
    ('date', c_double),
    ('bstrVal', POINTER(_FLAGGED_WORD_BLOB)),
    ('punkVal', POINTER(IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('parray', POINTER(POINTER(_wireSAFEARRAY))),
    ('brecVal', POINTER(_wireBRECORD)),
    ('pbVal', POINTER(c_ubyte)),
    ('piVal', POINTER(c_short)),
    ('plVal', POINTER(c_int)),
    ('pllVal', POINTER(c_longlong)),
    ('pfltVal', POINTER(c_float)),
    ('pdblVal', POINTER(c_double)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(c_longlong)),
    ('pdate', POINTER(c_double)),
    ('pbstrVal', POINTER(POINTER(_FLAGGED_WORD_BLOB))),
    ('ppunkVal', POINTER(POINTER(IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(POINTER(POINTER(_wireSAFEARRAY)))),
    ('pvarVal', POINTER(POINTER(_wireVARIANT))),
    ('cVal', c_char),
    ('uiVal', c_ushort),
    ('ulVal', c_ulong),
    ('ullVal', c_ulonglong),
    ('intVal', c_int),
    ('uintVal', c_uint),
    ('decVal', DECIMAL),
    ('pdecVal', POINTER(DECIMAL)),
    ('pcVal', STRING),
    ('puiVal', POINTER(c_ushort)),
    ('pulVal', POINTER(c_ulong)),
    ('pullVal', POINTER(c_ulonglong)),
    ('pintVal', POINTER(c_int)),
    ('puintVal', POINTER(c_uint)),
]
assert sizeof(__MIDL_IOleAutomationTypes_0004) == 16, sizeof(__MIDL_IOleAutomationTypes_0004)
assert alignment(__MIDL_IOleAutomationTypes_0004) == 8, alignment(__MIDL_IOleAutomationTypes_0004)
_wireVARIANT._fields_ = [
    ('clSize', c_ulong),
    ('rpcReserved', c_ulong),
    ('vt', c_ushort),
    ('wReserved1', c_ushort),
    ('wReserved2', c_ushort),
    ('wReserved3', c_ushort),
    ('DUMMYUNIONNAME', __MIDL_IOleAutomationTypes_0004),
]
assert sizeof(_wireVARIANT) == 32, sizeof(_wireVARIANT)
assert alignment(_wireVARIANT) == 8, alignment(_wireVARIANT)
class ITaskbarList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56FDF342-FD6D-11D0-958A-006097C9A090}')
    _idlflags_ = []
class ITaskbarList2(ITaskbarList):
    _case_insensitive_ = True
    _iid_ = GUID('{602D4995-B13A-429B-A66E-1935E44F4317}')
    _idlflags_ = []
ITaskbarList._methods_ = [
    COMMETHOD([], HRESULT, 'HrInit'),
    COMMETHOD([], HRESULT, 'AddTab',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'DeleteTab',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'ActivateTab',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'SetActiveAlt',
              ( ['in'], wireHWND, 'hwnd' )),
]
################################################################
## code template for ITaskbarList implementation
##class ITaskbarList_Impl(object):
##    def HrInit(self):
##        '-no docstring-'
##        #return
##
##    def AddTab(self, hwnd):
##        '-no docstring-'
##        #return
##
##    def DeleteTab(self, hwnd):
##        '-no docstring-'
##        #return
##
##    def ActivateTab(self, hwnd):
##        '-no docstring-'
##        #return
##
##    def SetActiveAlt(self, hwnd):
##        '-no docstring-'
##        #return
##

ITaskbarList2._methods_ = [
    COMMETHOD([], HRESULT, 'MarkFullscreenWindow',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_int, 'fFullscreen' )),
]
################################################################
## code template for ITaskbarList2 implementation
##class ITaskbarList2_Impl(object):
##    def MarkFullscreenWindow(self, hwnd, fFullscreen):
##        '-no docstring-'
##        #return
##

IContextMenuCB._methods_ = [
    COMMETHOD([], HRESULT, 'CallBack',
              ( ['in'], POINTER(IShellFolder), 'psf' ),
              ( ['in'], wireHWND, 'hwndOwner' ),
              ( ['in'], POINTER(IDataObject), 'pdtobj' ),
              ( ['in'], c_uint, 'uMsg' ),
              ( ['in'], UINT_PTR, 'wParam' ),
              ( ['in'], LONG_PTR, 'lParam' )),
]
################################################################
## code template for IContextMenuCB implementation
##class IContextMenuCB_Impl(object):
##    def CallBack(self, psf, hwndOwner, pdtobj, uMsg, wParam, lParam):
##        '-no docstring-'
##        #return
##

class IShellItem2(IShellItem):
    _case_insensitive_ = True
    _iid_ = GUID('{7E9FB0D3-919F-4307-AB2E-9B1860310C93}')
    _idlflags_ = []

# values for enumeration '_SIGDN'
SIGDN_NORMALDISPLAY = 0
SIGDN_PARENTRELATIVEPARSING = -2147385343
SIGDN_DESKTOPABSOLUTEPARSING = -2147319808
SIGDN_PARENTRELATIVEEDITING = -2147282943
SIGDN_DESKTOPABSOLUTEEDITING = -2147172352
SIGDN_FILESYSPATH = -2147123200
SIGDN_URL = -2147057664
SIGDN_PARENTRELATIVEFORADDRESSBAR = -2146975743
SIGDN_PARENTRELATIVE = -2146959359
SIGDN_PARENTRELATIVEFORUI = -2146877439
_SIGDN = c_int # enum
IShellItem._methods_ = [
    COMMETHOD([], HRESULT, 'BindToHandler',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(GUID), 'bhid' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetParent',
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsi' )),
    COMMETHOD([], HRESULT, 'GetDisplayName',
              ( ['in'], _SIGDN, 'sigdnName' ),
              ( ['out'], POINTER(WSTRING), 'ppszName' )),
    COMMETHOD([], HRESULT, 'GetAttributes',
              ( ['in'], c_ulong, 'sfgaoMask' ),
              ( ['out'], POINTER(c_ulong), 'psfgaoAttribs' )),
    COMMETHOD([], HRESULT, 'Compare',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], c_ulong, 'hint' ),
              ( ['out'], POINTER(c_int), 'piOrder' )),
]
################################################################
## code template for IShellItem implementation
##class IShellItem_Impl(object):
##    def BindToHandler(self, pbc, bhid, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetParent(self):
##        '-no docstring-'
##        #return ppsi
##
##    def GetDisplayName(self, sigdnName):
##        '-no docstring-'
##        #return ppszName
##
##    def GetAttributes(self, sfgaoMask):
##        '-no docstring-'
##        #return psfgaoAttribs
##
##    def Compare(self, psi, hint):
##        '-no docstring-'
##        #return piOrder
##

IShellItem2._methods_ = [
    COMMETHOD([], HRESULT, 'GetPropertyStore',
              ( ['in'], GETPROPERTYSTOREFLAGS, 'Flags' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetPropertyStoreWithCreateObject',
              ( ['in'], GETPROPERTYSTOREFLAGS, 'Flags' ),
              ( ['in'], POINTER(IUnknown), 'punkCreateObject' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetPropertyStoreForKeys',
              ( ['in'], POINTER(_tagpropertykey), 'rgKeys' ),
              ( ['in'], c_uint, 'cKeys' ),
              ( ['in'], GETPROPERTYSTOREFLAGS, 'Flags' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetPropertyDescriptionList',
              ( ['in'], POINTER(_tagpropertykey), 'keyType' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'Update',
              ( ['in'], POINTER(IBindCtx), 'pbc' )),
    COMMETHOD([], HRESULT, 'GetProperty',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'ppropvar' )),
    COMMETHOD([], HRESULT, 'GetCLSID',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(GUID), 'pclsid' )),
    COMMETHOD([], HRESULT, 'GetFileTime',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(_FILETIME), 'pft' )),
    COMMETHOD([], HRESULT, 'GetInt32',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_int), 'pi' )),
    COMMETHOD([], HRESULT, 'GetString',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(WSTRING), 'ppsz' )),
    COMMETHOD([], HRESULT, 'GetUInt32',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_ulong), 'pui' )),
    COMMETHOD([], HRESULT, 'GetUInt64',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_ulonglong), 'pull' )),
    COMMETHOD([], HRESULT, 'GetBool',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(c_int), 'pf' )),
]
################################################################
## code template for IShellItem2 implementation
##class IShellItem2_Impl(object):
##    def GetPropertyStore(self, Flags, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetPropertyStoreWithCreateObject(self, Flags, punkCreateObject, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetPropertyStoreForKeys(self, rgKeys, cKeys, Flags, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetPropertyDescriptionList(self, keyType, riid):
##        '-no docstring-'
##        #return ppv
##
##    def Update(self, pbc):
##        '-no docstring-'
##        #return
##
##    def GetProperty(self, key):
##        '-no docstring-'
##        #return ppropvar
##
##    def GetCLSID(self, key):
##        '-no docstring-'
##        #return pclsid
##
##    def GetFileTime(self, key):
##        '-no docstring-'
##        #return pft
##
##    def GetInt32(self, key):
##        '-no docstring-'
##        #return pi
##
##    def GetString(self, key):
##        '-no docstring-'
##        #return ppsz
##
##    def GetUInt32(self, key):
##        '-no docstring-'
##        #return pui
##
##    def GetUInt64(self, key):
##        '-no docstring-'
##        #return pull
##
##    def GetBool(self, key):
##        '-no docstring-'
##        #return pf
##

_userHBITMAP._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0007),
]
assert sizeof(_userHBITMAP) == 16, sizeof(_userHBITMAP)
assert alignment(_userHBITMAP) == 8, alignment(_userHBITMAP)
class FrameworkInputPane(CoClass):
    _reg_clsid_ = GUID('{D5120AA3-46BA-44C5-822D-CA8092C1FC72}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
FrameworkInputPane._com_interfaces_ = [IFrameworkInputPane]

IQueryContinue._methods_ = [
    COMMETHOD([], HRESULT, 'QueryContinue'),
]
################################################################
## code template for IQueryContinue implementation
##class IQueryContinue_Impl(object):
##    def QueryContinue(self):
##        '-no docstring-'
##        #return
##

class PropertiesUI(CoClass):
    _reg_clsid_ = GUID('{D912F8CF-0396-4915-884E-FB425D32943B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IPropertyUI(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{757A7D9F-919A-4118-99D7-DBB208C8CC66}')
    _idlflags_ = []
PropertiesUI._com_interfaces_ = [IPropertyUI]


# values for enumeration 'NATIVE_DISPLAY_ORIENTATION'
NDO_LANDSCAPE = 0
NDO_PORTRAIT = 1
NATIVE_DISPLAY_ORIENTATION = c_int # enum

# values for enumeration 'APPDOCLISTTYPE'
ADLT_RECENT = 0
ADLT_FREQUENT = 1
APPDOCLISTTYPE = c_int # enum
IApplicationDocumentLists._methods_ = [
    COMMETHOD([], HRESULT, 'SetAppID',
              ( ['in'], WSTRING, 'pszAppID' )),
    COMMETHOD([], HRESULT, 'GetList',
              ( ['in'], APPDOCLISTTYPE, 'listtype' ),
              ( ['in'], c_uint, 'cItemsDesired' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
]
################################################################
## code template for IApplicationDocumentLists implementation
##class IApplicationDocumentLists_Impl(object):
##    def SetAppID(self, pszAppID):
##        '-no docstring-'
##        #return
##
##    def GetList(self, listtype, cItemsDesired, riid):
##        '-no docstring-'
##        #return ppv
##


# values for enumeration 'STPFLAG'
STPF_NONE = 0
STPF_USEAPPTHUMBNAILALWAYS = 1
STPF_USEAPPTHUMBNAILWHENACTIVE = 2
STPF_USEAPPPEEKALWAYS = 4
STPF_USEAPPPEEKWHENACTIVE = 8
STPFLAG = c_int # enum
IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return
##
##    def Revert(self):
##        '-no docstring-'
##        #return
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##

_COMDLG_FILTERSPEC._fields_ = [
    ('pszName', WSTRING),
    ('pszSpec', WSTRING),
]
assert sizeof(_COMDLG_FILTERSPEC) == 8, sizeof(_COMDLG_FILTERSPEC)
assert alignment(_COMDLG_FILTERSPEC) == 4, alignment(_COMDLG_FILTERSPEC)
IRichChunk._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteGetData',
              ( ['out'], POINTER(c_ulong), 'pFirstPos' ),
              ( ['out'], POINTER(c_ulong), 'pLength' ),
              ( ['out'], POINTER(WSTRING), 'ppsz' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'pValue' )),
]
################################################################
## code template for IRichChunk implementation
##class IRichChunk_Impl(object):
##    def RemoteGetData(self):
##        '-no docstring-'
##        #return pFirstPos, pLength, ppsz, pValue
##

IRunningObjectTable._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], c_ulong, 'grfFlags' ),
              ( ['in'], POINTER(IUnknown), 'punkObject' ),
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(c_ulong), 'pdwRegister' )),
    COMMETHOD([], HRESULT, 'Revoke',
              ( ['in'], c_ulong, 'dwRegister' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' )),
    COMMETHOD([], HRESULT, 'GetObject',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunkObject' )),
    COMMETHOD([], HRESULT, 'NoteChangeTime',
              ( ['in'], c_ulong, 'dwRegister' ),
              ( ['in'], POINTER(_FILETIME), 'pFileTime' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(_FILETIME), 'pFileTime' )),
    COMMETHOD([], HRESULT, 'EnumRunning',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
]
################################################################
## code template for IRunningObjectTable implementation
##class IRunningObjectTable_Impl(object):
##    def Register(self, grfFlags, punkObject, pmkObjectName):
##        '-no docstring-'
##        #return pdwRegister
##
##    def Revoke(self, dwRegister):
##        '-no docstring-'
##        #return
##
##    def IsRunning(self, pmkObjectName):
##        '-no docstring-'
##        #return
##
##    def GetObject(self, pmkObjectName):
##        '-no docstring-'
##        #return ppunkObject
##
##    def NoteChangeTime(self, dwRegister, pFileTime):
##        '-no docstring-'
##        #return
##
##    def GetTimeOfLastChange(self, pmkObjectName):
##        '-no docstring-'
##        #return pFileTime
##
##    def EnumRunning(self):
##        '-no docstring-'
##        #return ppenumMoniker
##

class FreeSpaceCategorizer(CoClass):
    _reg_clsid_ = GUID('{B5607793-24AC-44C7-82E2-831726AA6CB7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
FreeSpaceCategorizer._com_interfaces_ = [ICategorizer]

class ITaskbarList3(ITaskbarList2):
    _case_insensitive_ = True
    _iid_ = GUID('{EA1AFB91-9E28-4B86-90E9-9E9F8A5EEFAF}')
    _idlflags_ = []
ITaskbarList3._methods_ = [
    COMMETHOD([], HRESULT, 'SetProgressValue',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_ulonglong, 'ullCompleted' ),
              ( ['in'], c_ulonglong, 'ullTotal' )),
    COMMETHOD([], HRESULT, 'SetProgressState',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], TBPFLAG, 'tbpFlags' )),
    COMMETHOD([], HRESULT, 'RegisterTab',
              ( ['in'], wireHWND, 'hwndTab' ),
              ( ['in'], wireHWND, 'hwndMDI' )),
    COMMETHOD([], HRESULT, 'UnregisterTab',
              ( ['in'], wireHWND, 'hwndTab' )),
    COMMETHOD([], HRESULT, 'SetTabOrder',
              ( ['in'], wireHWND, 'hwndTab' ),
              ( ['in'], wireHWND, 'hwndInsertBefore' )),
    COMMETHOD([], HRESULT, 'SetTabActive',
              ( ['in'], wireHWND, 'hwndTab' ),
              ( ['in'], wireHWND, 'hwndMDI' ),
              ( ['in'], c_ulong, 'dwReserved' )),
    COMMETHOD([], HRESULT, 'ThumbBarAddButtons',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_uint, 'cButtons' ),
              ( ['in'], POINTER(THUMBBUTTON), 'pButton' )),
    COMMETHOD([], HRESULT, 'ThumbBarUpdateButtons',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_uint, 'cButtons' ),
              ( ['in'], POINTER(THUMBBUTTON), 'pButton' )),
    COMMETHOD([], HRESULT, 'ThumbBarSetImageList',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(IUnknown), 'himl' )),
    COMMETHOD([], HRESULT, 'SetOverlayIcon',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], wireHICON, 'hIcon' ),
              ( ['in'], WSTRING, 'pszDescription' )),
    COMMETHOD([], HRESULT, 'SetThumbnailTooltip',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], WSTRING, 'pszTip' )),
    COMMETHOD([], HRESULT, 'SetThumbnailClip',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(tagRECT), 'prcClip' )),
]
################################################################
## code template for ITaskbarList3 implementation
##class ITaskbarList3_Impl(object):
##    def SetProgressValue(self, hwnd, ullCompleted, ullTotal):
##        '-no docstring-'
##        #return
##
##    def SetProgressState(self, hwnd, tbpFlags):
##        '-no docstring-'
##        #return
##
##    def RegisterTab(self, hwndTab, hwndMDI):
##        '-no docstring-'
##        #return
##
##    def UnregisterTab(self, hwndTab):
##        '-no docstring-'
##        #return
##
##    def SetTabOrder(self, hwndTab, hwndInsertBefore):
##        '-no docstring-'
##        #return
##
##    def SetTabActive(self, hwndTab, hwndMDI, dwReserved):
##        '-no docstring-'
##        #return
##
##    def ThumbBarAddButtons(self, hwnd, cButtons, pButton):
##        '-no docstring-'
##        #return
##
##    def ThumbBarUpdateButtons(self, hwnd, cButtons, pButton):
##        '-no docstring-'
##        #return
##
##    def ThumbBarSetImageList(self, hwnd, himl):
##        '-no docstring-'
##        #return
##
##    def SetOverlayIcon(self, hwnd, hIcon, pszDescription):
##        '-no docstring-'
##        #return
##
##    def SetThumbnailTooltip(self, hwnd, pszTip):
##        '-no docstring-'
##        #return
##
##    def SetThumbnailClip(self, hwnd, prcClip):
##        '-no docstring-'
##        #return
##

class ShellItem(CoClass):
    _reg_clsid_ = GUID('{9AC9FBE1-E0A2-4AD6-B4EE-E212013EA917}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ShellItem._com_interfaces_ = [IShellItem2]

IPropertyUI._methods_ = [
    COMMETHOD([], HRESULT, 'ParsePropertyName',
              ( ['in'], WSTRING, 'pszName' ),
              ( ['out'], POINTER(GUID), 'pfmtid' ),
              ( ['out'], POINTER(c_ulong), 'ppid' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pchEaten' )),
    COMMETHOD([], HRESULT, 'GetCannonicalName',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['out'], WSTRING, 'pwszText' ),
              ( ['in'], c_ulong, 'cchText' )),
    COMMETHOD([], HRESULT, 'GetDisplayName',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['in'], c_ulong, 'Flags' ),
              ( ['out'], WSTRING, 'pwszText' ),
              ( ['in'], c_ulong, 'cchText' )),
    COMMETHOD([], HRESULT, 'GetPropertyDescription',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['out'], WSTRING, 'pwszText' ),
              ( ['in'], c_ulong, 'cchText' )),
    COMMETHOD([], HRESULT, 'GetDefaultWidth',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['out'], POINTER(c_ulong), 'pcxChars' )),
    COMMETHOD([], HRESULT, 'GetFlags',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['out'], POINTER(c_ulong), 'pflags' )),
    COMMETHOD([], HRESULT, 'FormatForDisplay',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'ppropvar' ),
              ( ['in'], c_ulong, 'puiff' ),
              ( ['out'], WSTRING, 'pwszText' ),
              ( ['in'], c_ulong, 'cchText' )),
    COMMETHOD([], HRESULT, 'GetHelpInfo',
              ( ['in'], POINTER(GUID), 'fmtid' ),
              ( ['in'], c_ulong, 'pid' ),
              ( ['out'], WSTRING, 'pwszHelpFile' ),
              ( ['in'], c_ulong, 'cch' ),
              ( ['out'], POINTER(c_uint), 'puHelpID' )),
]
################################################################
## code template for IPropertyUI implementation
##class IPropertyUI_Impl(object):
##    def ParsePropertyName(self, pszName):
##        '-no docstring-'
##        #return pfmtid, ppid, pchEaten
##
##    def GetCannonicalName(self, fmtid, pid, cchText):
##        '-no docstring-'
##        #return pwszText
##
##    def GetDisplayName(self, fmtid, pid, Flags, cchText):
##        '-no docstring-'
##        #return pwszText
##
##    def GetPropertyDescription(self, fmtid, pid, cchText):
##        '-no docstring-'
##        #return pwszText
##
##    def GetDefaultWidth(self, fmtid, pid):
##        '-no docstring-'
##        #return pcxChars
##
##    def GetFlags(self, fmtid, pid):
##        '-no docstring-'
##        #return pflags
##
##    def FormatForDisplay(self, fmtid, pid, ppropvar, puiff, cchText):
##        '-no docstring-'
##        #return pwszText
##
##    def GetHelpInfo(self, fmtid, pid, cch):
##        '-no docstring-'
##        #return pwszHelpFile, puHelpID
##

class IHomeGroup(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7A3BD1D9-35A9-4FB3-A467-F48CAC35E2D0}')
    _idlflags_ = []

# values for enumeration 'HOMEGROUPSHARINGCHOICES'
HGSC_NONE = 0
HGSC_MUSICLIBRARY = 1
HGSC_PICTURESLIBRARY = 2
HGSC_VIDEOSLIBRARY = 4
HGSC_DOCUMENTSLIBRARY = 8
HGSC_PRINTERS = 16
HOMEGROUPSHARINGCHOICES = c_int # enum
IHomeGroup._methods_ = [
    COMMETHOD([], HRESULT, 'IsMember',
              ( ['out'], POINTER(c_int), 'member' )),
    COMMETHOD([], HRESULT, 'ShowSharingWizard',
              ( ['in'], wireHWND, 'owner' ),
              ( ['out'], POINTER(HOMEGROUPSHARINGCHOICES), 'sharingchoices' )),
]
################################################################
## code template for IHomeGroup implementation
##class IHomeGroup_Impl(object):
##    def IsMember(self):
##        '-no docstring-'
##        #return member
##
##    def ShowSharingWizard(self, owner):
##        '-no docstring-'
##        #return sharingchoices
##

class UserNotification(CoClass):
    _reg_clsid_ = GUID('{0010890E-8789-413C-ADBC-48F5B511B3AF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
UserNotification._com_interfaces_ = [IUserNotification]

class ITaskbarList4(ITaskbarList3):
    _case_insensitive_ = True
    _iid_ = GUID('{C43DC798-95D1-4BEA-9030-BB99E2983A1A}')
    _idlflags_ = []
ITaskbarList4._methods_ = [
    COMMETHOD([], HRESULT, 'SetTabProperties',
              ( ['in'], wireHWND, 'hwndTab' ),
              ( ['in'], STPFLAG, 'stpFlags' )),
]
################################################################
## code template for ITaskbarList4 implementation
##class ITaskbarList4_Impl(object):
##    def SetTabProperties(self, hwndTab, stpFlags):
##        '-no docstring-'
##        #return
##


# values for enumeration 'FDE_SHAREVIOLATION_RESPONSE'
FDESVR_DEFAULT = 0
FDESVR_ACCEPT = 1
FDESVR_REFUSE = 2
FDE_SHAREVIOLATION_RESPONSE = c_int # enum

# values for enumeration 'FDE_OVERWRITE_RESPONSE'
FDEOR_DEFAULT = 0
FDEOR_ACCEPT = 1
FDEOR_REFUSE = 2
FDE_OVERWRITE_RESPONSE = c_int # enum
IFileDialogEvents._methods_ = [
    COMMETHOD([], HRESULT, 'OnFileOk',
              ( ['in'], POINTER(IFileDialog), 'pfd' )),
    COMMETHOD([], HRESULT, 'OnFolderChanging',
              ( ['in'], POINTER(IFileDialog), 'pfd' ),
              ( ['in'], POINTER(IShellItem), 'psiFolder' )),
    COMMETHOD([], HRESULT, 'OnFolderChange',
              ( ['in'], POINTER(IFileDialog), 'pfd' )),
    COMMETHOD([], HRESULT, 'OnSelectionChange',
              ( ['in'], POINTER(IFileDialog), 'pfd' )),
    COMMETHOD([], HRESULT, 'OnShareViolation',
              ( ['in'], POINTER(IFileDialog), 'pfd' ),
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['out'], POINTER(FDE_SHAREVIOLATION_RESPONSE), 'pResponse' )),
    COMMETHOD([], HRESULT, 'OnTypeChange',
              ( ['in'], POINTER(IFileDialog), 'pfd' )),
    COMMETHOD([], HRESULT, 'OnOverwrite',
              ( ['in'], POINTER(IFileDialog), 'pfd' ),
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['out'], POINTER(FDE_OVERWRITE_RESPONSE), 'pResponse' )),
]
################################################################
## code template for IFileDialogEvents implementation
##class IFileDialogEvents_Impl(object):
##    def OnFileOk(self, pfd):
##        '-no docstring-'
##        #return
##
##    def OnFolderChanging(self, pfd, psiFolder):
##        '-no docstring-'
##        #return
##
##    def OnFolderChange(self, pfd):
##        '-no docstring-'
##        #return
##
##    def OnSelectionChange(self, pfd):
##        '-no docstring-'
##        #return
##
##    def OnShareViolation(self, pfd, psi):
##        '-no docstring-'
##        #return pResponse
##
##    def OnTypeChange(self, pfd):
##        '-no docstring-'
##        #return
##
##    def OnOverwrite(self, pfd, psi):
##        '-no docstring-'
##        #return pResponse
##

_userBITMAP._fields_ = [
    ('bmType', c_int),
    ('bmWidth', c_int),
    ('bmHeight', c_int),
    ('bmWidthBytes', c_int),
    ('bmPlanes', c_ushort),
    ('bmBitsPixel', c_ushort),
    ('cbSize', c_ulong),
    ('pBuffer', POINTER(c_ubyte)),
]
assert sizeof(_userBITMAP) == 28, sizeof(_userBITMAP)
assert alignment(_userBITMAP) == 4, alignment(_userBITMAP)
class DefFolderMenu(CoClass):
    _reg_clsid_ = GUID('{C63382BE-7933-48D0-9AC8-85FB46BE2FDD}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
DefFolderMenu._com_interfaces_ = [IDefaultFolderMenuInitialize]

class TaskbarList(CoClass):
    _reg_clsid_ = GUID('{56FDF344-FD6D-11D0-958A-006097C9A090}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
TaskbarList._com_interfaces_ = [ITaskbarList4]

class ApplicationAssociationRegistration(CoClass):
    _reg_clsid_ = GUID('{591209C7-767B-42B2-9FBA-44EE4615F2C7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IApplicationAssociationRegistration(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4E530B0A-E611-4C77-A3AC-9031D022281B}')
    _idlflags_ = []
ApplicationAssociationRegistration._com_interfaces_ = [IApplicationAssociationRegistration]

class _STGMEDIUM_UNION(Structure):
    pass
class __MIDL_IAdviseSink_0003(Union):
    pass
__MIDL_IAdviseSink_0003._fields_ = [
    ('hMetaFilePict', POINTER(_userHMETAFILEPICT)),
    ('hHEnhMetaFile', POINTER(_userHENHMETAFILE)),
    ('hGdiHandle', POINTER(_GDI_OBJECT)),
    ('hGlobal', POINTER(_userHGLOBAL)),
    ('lpszFileName', WSTRING),
    ('pstm', POINTER(_BYTE_BLOB)),
    ('pstg', POINTER(_BYTE_BLOB)),
]
assert sizeof(__MIDL_IAdviseSink_0003) == 4, sizeof(__MIDL_IAdviseSink_0003)
assert alignment(__MIDL_IAdviseSink_0003) == 4, alignment(__MIDL_IAdviseSink_0003)
_STGMEDIUM_UNION._fields_ = [
    ('tymed', c_ulong),
    ('u', __MIDL_IAdviseSink_0003),
]
assert sizeof(_STGMEDIUM_UNION) == 8, sizeof(_STGMEDIUM_UNION)
assert alignment(_STGMEDIUM_UNION) == 4, alignment(_STGMEDIUM_UNION)
_userSTGMEDIUM._fields_ = [
    ('DUMMYUNIONNAME', _STGMEDIUM_UNION),
    ('pUnkForRelease', POINTER(IUnknown)),
]
assert sizeof(_userSTGMEDIUM) == 12, sizeof(_userSTGMEDIUM)
assert alignment(_userSTGMEDIUM) == 4, alignment(_userSTGMEDIUM)
class ScheduledTasks(CoClass):
    _reg_clsid_ = GUID('{D6277990-4C6A-11CF-8D87-00AA0060F5BF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ScheduledTasks._com_interfaces_ = [IShellFolder2]

class __MIDL_IWinTypes_0008(Union):
    pass
class tagLOGPALETTE(Structure):
    pass
__MIDL_IWinTypes_0008._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(tagLOGPALETTE)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0008) == 8, sizeof(__MIDL_IWinTypes_0008)
assert alignment(__MIDL_IWinTypes_0008) == 8, alignment(__MIDL_IWinTypes_0008)
_userHPALETTE._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0008),
]
assert sizeof(_userHPALETTE) == 16, sizeof(_userHPALETTE)
assert alignment(_userHPALETTE) == 8, alignment(_userHPALETTE)
class INamespaceWalkCB(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D92995F8-CF5E-4A76-BF59-EAD39EA2B97E}')
    _idlflags_ = []
INamespaceWalkCB._methods_ = [
    COMMETHOD([], HRESULT, 'FoundItem',
              ( ['in'], POINTER(IShellFolder), 'psf' ),
              ( ['in'], wirePIDL, 'pidl' )),
    COMMETHOD([], HRESULT, 'EnterFolder',
              ( ['in'], POINTER(IShellFolder), 'psf' ),
              ( ['in'], wirePIDL, 'pidl' )),
    COMMETHOD([], HRESULT, 'LeaveFolder',
              ( ['in'], POINTER(IShellFolder), 'psf' ),
              ( ['in'], wirePIDL, 'pidl' )),
    COMMETHOD([], HRESULT, 'InitializeProgressDialog',
              ( ['out'], POINTER(WSTRING), 'ppszTitle' ),
              ( ['out'], POINTER(WSTRING), 'ppszCancel' )),
]
################################################################
## code template for INamespaceWalkCB implementation
##class INamespaceWalkCB_Impl(object):
##    def FoundItem(self, psf, pidl):
##        '-no docstring-'
##        #return
##
##    def EnterFolder(self, psf, pidl):
##        '-no docstring-'
##        #return
##
##    def LeaveFolder(self, psf, pidl):
##        '-no docstring-'
##        #return
##
##    def InitializeProgressDialog(self):
##        '-no docstring-'
##        #return ppszTitle, ppszCancel
##

class HomeGroup(CoClass):
    _reg_clsid_ = GUID('{DE77BA04-3C92-4D11-A1A5-42352A53E0E3}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
HomeGroup._com_interfaces_ = [IHomeGroup]

IMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteBindToObject',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(GUID), 'riidResult' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvResult' )),
    COMMETHOD([], HRESULT, 'RemoteBindToStorage',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvObj' )),
    COMMETHOD([], HRESULT, 'Reduce',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], c_ulong, 'dwReduceHowFar' ),
              ( ['in', 'out'], POINTER(POINTER(IMoniker)), 'ppmkToLeft' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkReduced' )),
    COMMETHOD([], HRESULT, 'ComposeWith',
              ( ['in'], POINTER(IMoniker), 'pmkRight' ),
              ( ['in'], c_int, 'fOnlyIfNotGeneric' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkComposite' )),
    COMMETHOD([], HRESULT, 'Enum',
              ( ['in'], c_int, 'fForward' ),
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
    COMMETHOD([], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IMoniker), 'pmkOtherMoniker' )),
    COMMETHOD([], HRESULT, 'Hash',
              ( ['out'], POINTER(c_ulong), 'pdwHash' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(IMoniker), 'pmkNewlyRunning' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(_FILETIME), 'pFileTime' )),
    COMMETHOD([], HRESULT, 'Inverse',
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmk' )),
    COMMETHOD([], HRESULT, 'CommonPrefixWith',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkPrefix' )),
    COMMETHOD([], HRESULT, 'RelativePathTo',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkRelPath' )),
    COMMETHOD([], HRESULT, 'GetDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(WSTRING), 'ppszDisplayName' )),
    COMMETHOD([], HRESULT, 'ParseDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], WSTRING, 'pszDisplayName' ),
              ( ['out'], POINTER(c_ulong), 'pchEaten' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkOut' )),
    COMMETHOD([], HRESULT, 'IsSystemMoniker',
              ( ['out'], POINTER(c_ulong), 'pdwMksys' )),
]
################################################################
## code template for IMoniker implementation
##class IMoniker_Impl(object):
##    def RemoteBindToObject(self, pbc, pmkToLeft, riidResult):
##        '-no docstring-'
##        #return ppvResult
##
##    def RemoteBindToStorage(self, pbc, pmkToLeft, riid):
##        '-no docstring-'
##        #return ppvObj
##
##    def Reduce(self, pbc, dwReduceHowFar):
##        '-no docstring-'
##        #return ppmkToLeft, ppmkReduced
##
##    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric):
##        '-no docstring-'
##        #return ppmkComposite
##
##    def Enum(self, fForward):
##        '-no docstring-'
##        #return ppenumMoniker
##
##    def IsEqual(self, pmkOtherMoniker):
##        '-no docstring-'
##        #return
##
##    def Hash(self):
##        '-no docstring-'
##        #return pdwHash
##
##    def IsRunning(self, pbc, pmkToLeft, pmkNewlyRunning):
##        '-no docstring-'
##        #return
##
##    def GetTimeOfLastChange(self, pbc, pmkToLeft):
##        '-no docstring-'
##        #return pFileTime
##
##    def Inverse(self):
##        '-no docstring-'
##        #return ppmk
##
##    def CommonPrefixWith(self, pmkOther):
##        '-no docstring-'
##        #return ppmkPrefix
##
##    def RelativePathTo(self, pmkOther):
##        '-no docstring-'
##        #return ppmkRelPath
##
##    def GetDisplayName(self, pbc, pmkToLeft):
##        '-no docstring-'
##        #return ppszDisplayName
##
##    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName):
##        '-no docstring-'
##        #return pchEaten, ppmkOut
##
##    def IsSystemMoniker(self):
##        '-no docstring-'
##        #return pdwMksys
##


# values for enumeration 'ASSOCIATIONTYPE'
AT_FILEEXTENSION = 0
AT_URLPROTOCOL = 1
AT_STARTMENUCLIENT = 2
AT_MIMETYPE = 3
ASSOCIATIONTYPE = c_int # enum
IApplicationAssociationRegistration._methods_ = [
    COMMETHOD([], HRESULT, 'QueryCurrentDefault',
              ( ['in'], WSTRING, 'pszQuery' ),
              ( ['in'], ASSOCIATIONTYPE, 'atQueryType' ),
              ( ['in'], ASSOCIATIONLEVEL, 'alQueryLevel' ),
              ( ['out'], POINTER(WSTRING), 'ppszAssociation' )),
    COMMETHOD([], HRESULT, 'QueryAppIsDefault',
              ( ['in'], WSTRING, 'pszQuery' ),
              ( ['in'], ASSOCIATIONTYPE, 'atQueryType' ),
              ( ['in'], ASSOCIATIONLEVEL, 'alQueryLevel' ),
              ( ['in'], WSTRING, 'pszAppRegistryName' ),
              ( ['out'], POINTER(c_int), 'pfDefault' )),
    COMMETHOD([], HRESULT, 'QueryAppIsDefaultAll',
              ( ['in'], ASSOCIATIONLEVEL, 'alQueryLevel' ),
              ( ['in'], WSTRING, 'pszAppRegistryName' ),
              ( ['out'], POINTER(c_int), 'pfDefault' )),
    COMMETHOD([], HRESULT, 'SetAppAsDefault',
              ( ['in'], WSTRING, 'pszAppRegistryName' ),
              ( ['in'], WSTRING, 'pszSet' ),
              ( ['in'], ASSOCIATIONTYPE, 'atSetType' )),
    COMMETHOD([], HRESULT, 'SetAppAsDefaultAll',
              ( ['in'], WSTRING, 'pszAppRegistryName' )),
    COMMETHOD([], HRESULT, 'ClearUserAssociations'),
]
################################################################
## code template for IApplicationAssociationRegistration implementation
##class IApplicationAssociationRegistration_Impl(object):
##    def QueryCurrentDefault(self, pszQuery, atQueryType, alQueryLevel):
##        '-no docstring-'
##        #return ppszAssociation
##
##    def QueryAppIsDefault(self, pszQuery, atQueryType, alQueryLevel, pszAppRegistryName):
##        '-no docstring-'
##        #return pfDefault
##
##    def QueryAppIsDefaultAll(self, alQueryLevel, pszAppRegistryName):
##        '-no docstring-'
##        #return pfDefault
##
##    def SetAppAsDefault(self, pszAppRegistryName, pszSet, atSetType):
##        '-no docstring-'
##        #return
##
##    def SetAppAsDefaultAll(self, pszAppRegistryName):
##        '-no docstring-'
##        #return
##
##    def ClearUserAssociations(self):
##        '-no docstring-'
##        #return
##

class __MIDL_IOleAutomationTypes_0006(Union):
    pass
__MIDL_IOleAutomationTypes_0006._fields_ = [
    ('oInst', c_ulong),
    ('lpvarValue', POINTER(VARIANT)),
]
assert sizeof(__MIDL_IOleAutomationTypes_0006) == 4, sizeof(__MIDL_IOleAutomationTypes_0006)
assert alignment(__MIDL_IOleAutomationTypes_0006) == 4, alignment(__MIDL_IOleAutomationTypes_0006)
class __MIDL_IWinTypes_0003(Union):
    pass
class _FLAGGED_BYTE_BLOB(Structure):
    pass
__MIDL_IWinTypes_0003._fields_ = [
    ('hInproc', c_int),
    ('hRemote', POINTER(_FLAGGED_BYTE_BLOB)),
    ('hInproc64', c_longlong),
]
assert sizeof(__MIDL_IWinTypes_0003) == 8, sizeof(__MIDL_IWinTypes_0003)
assert alignment(__MIDL_IWinTypes_0003) == 8, alignment(__MIDL_IWinTypes_0003)
_userHGLOBAL._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0003),
]
assert sizeof(_userHGLOBAL) == 16, sizeof(_userHGLOBAL)
assert alignment(_userHGLOBAL) == 8, alignment(_userHGLOBAL)
class IShellLibrary(IUnknown):
    _case_insensitive_ = True
    'Shell Library API'
    _iid_ = GUID('{11A66EFA-382E-451A-9234-1E0E12EF3085}')
    _idlflags_ = []

# values for enumeration 'LIBRARYFOLDERFILTER'
LFF_FORCEFILESYSTEM = 1
LFF_STORAGEITEMS = 2
LFF_ALLITEMS = 3
LIBRARYFOLDERFILTER = c_int # enum

# values for enumeration 'DEFAULTSAVEFOLDERTYPE'
DSFT_DETECT = 1
DSFT_PRIVATE = 2
DSFT_PUBLIC = 3
DEFAULTSAVEFOLDERTYPE = c_int # enum

# values for enumeration 'LIBRARYOPTIONFLAGS'
LOF_DEFAULT = 0
LOF_PINNEDTONAVPANE = 1
LOF_MASK_ALL = 1
LIBRARYOPTIONFLAGS = c_int # enum

# values for enumeration 'LIBRARYSAVEFLAGS'
LSF_FAILIFTHERE = 0
LSF_OVERRIDEEXISTING = 1
LSF_MAKEUNIQUENAME = 2
LIBRARYSAVEFLAGS = c_int # enum
IShellLibrary._methods_ = [
    COMMETHOD([], HRESULT, 'LoadLibraryFromItem',
              ( ['in'], POINTER(IShellItem), 'psiLibrary' ),
              ( ['in'], c_ulong, 'grfMode' )),
    COMMETHOD([], HRESULT, 'LoadLibraryFromKnownFolder',
              ( ['in'], POINTER(GUID), 'kfidLibrary' ),
              ( ['in'], c_ulong, 'grfMode' )),
    COMMETHOD([], HRESULT, 'AddFolder',
              ( ['in'], POINTER(IShellItem), 'psiLocation' )),
    COMMETHOD([], HRESULT, 'RemoveFolder',
              ( ['in'], POINTER(IShellItem), 'psiLocation' )),
    COMMETHOD([], HRESULT, 'GetFolders',
              ( ['in'], LIBRARYFOLDERFILTER, 'lff' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'ResolveFolder',
              ( ['in'], POINTER(IShellItem), 'psiFolderToResolve' ),
              ( ['in'], c_ulong, 'dwTimeout' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetDefaultSaveFolder',
              ( ['in'], DEFAULTSAVEFOLDERTYPE, 'dsft' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'SetDefaultSaveFolder',
              ( ['in'], DEFAULTSAVEFOLDERTYPE, 'dsft' ),
              ( ['in'], POINTER(IShellItem), 'psi' )),
    COMMETHOD([], HRESULT, 'GetOptions',
              ( ['out'], POINTER(LIBRARYOPTIONFLAGS), 'plofOptions' )),
    COMMETHOD([], HRESULT, 'SetOptions',
              ( ['in'], LIBRARYOPTIONFLAGS, 'lofMask' ),
              ( ['in'], LIBRARYOPTIONFLAGS, 'lofOptions' )),
    COMMETHOD([], HRESULT, 'GetFolderType',
              ( ['out'], POINTER(GUID), 'pftid' )),
    COMMETHOD([], HRESULT, 'SetFolderType',
              ( ['in'], POINTER(GUID), 'ftid' )),
    COMMETHOD([], HRESULT, 'GetIcon',
              ( ['out'], POINTER(WSTRING), 'ppszIcon' )),
    COMMETHOD([], HRESULT, 'SetIcon',
              ( ['in'], WSTRING, 'pszIcon' )),
    COMMETHOD([], HRESULT, 'Commit'),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IShellItem), 'psiFolderToSaveIn' ),
              ( ['in'], WSTRING, 'pszLibraryName' ),
              ( ['in'], LIBRARYSAVEFLAGS, 'lsf' ),
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsiSavedTo' )),
    COMMETHOD([], HRESULT, 'SaveInKnownFolder',
              ( ['in'], POINTER(GUID), 'kfidToSaveIn' ),
              ( ['in'], WSTRING, 'pszLibraryName' ),
              ( ['in'], LIBRARYSAVEFLAGS, 'lsf' ),
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsiSavedTo' )),
]
################################################################
## code template for IShellLibrary implementation
##class IShellLibrary_Impl(object):
##    def LoadLibraryFromItem(self, psiLibrary, grfMode):
##        '-no docstring-'
##        #return
##
##    def LoadLibraryFromKnownFolder(self, kfidLibrary, grfMode):
##        '-no docstring-'
##        #return
##
##    def AddFolder(self, psiLocation):
##        '-no docstring-'
##        #return
##
##    def RemoveFolder(self, psiLocation):
##        '-no docstring-'
##        #return
##
##    def GetFolders(self, lff, riid):
##        '-no docstring-'
##        #return ppv
##
##    def ResolveFolder(self, psiFolderToResolve, dwTimeout, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetDefaultSaveFolder(self, dsft, riid):
##        '-no docstring-'
##        #return ppv
##
##    def SetDefaultSaveFolder(self, dsft, psi):
##        '-no docstring-'
##        #return
##
##    def GetOptions(self):
##        '-no docstring-'
##        #return plofOptions
##
##    def SetOptions(self, lofMask, lofOptions):
##        '-no docstring-'
##        #return
##
##    def GetFolderType(self):
##        '-no docstring-'
##        #return pftid
##
##    def SetFolderType(self, ftid):
##        '-no docstring-'
##        #return
##
##    def GetIcon(self):
##        '-no docstring-'
##        #return ppszIcon
##
##    def SetIcon(self, pszIcon):
##        '-no docstring-'
##        #return
##
##    def Commit(self):
##        '-no docstring-'
##        #return
##
##    def Save(self, psiFolderToSaveIn, pszLibraryName, lsf):
##        '-no docstring-'
##        #return ppsiSavedTo
##
##    def SaveInKnownFolder(self, kfidToSaveIn, pszLibraryName, lsf):
##        '-no docstring-'
##        #return ppsiSavedTo
##

class ShellLibrary(CoClass):
    _reg_clsid_ = GUID('{D9B3211D-E57F-4426-AAEF-30A806ADD397}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ShellLibrary._com_interfaces_ = [IShellLibrary]

_wireBRECORD._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('pRecInfo', POINTER(IRecordInfo)),
    ('pRecord', POINTER(c_ubyte)),
]
assert sizeof(_wireBRECORD) == 16, sizeof(_wireBRECORD)
assert alignment(_wireBRECORD) == 4, alignment(_wireBRECORD)
class AppStartupLink(CoClass):
    _reg_clsid_ = GUID('{273EB5E7-88B0-4843-BFEF-E2C81D43AAE5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IShellLinkW(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{000214F9-0000-0000-C000-000000000046}')
    _idlflags_ = []
AppStartupLink._com_interfaces_ = [IShellLinkW]

IAppVisibilityEvents._methods_ = [
    COMMETHOD([], HRESULT, 'AppVisibilityOnMonitorChanged',
              ( ['in'], wireHMONITOR, 'hMonitor' ),
              ( ['in'], MONITOR_APP_VISIBILITY, 'previousMode' ),
              ( ['in'], MONITOR_APP_VISIBILITY, 'currentMode' )),
    COMMETHOD([], HRESULT, 'LauncherVisibilityChange',
              ( ['in'], c_int, 'currentVisibleState' )),
]
################################################################
## code template for IAppVisibilityEvents implementation
##class IAppVisibilityEvents_Impl(object):
##    def AppVisibilityOnMonitorChanged(self, hMonitor, previousMode, currentMode):
##        '-no docstring-'
##        #return
##
##    def LauncherVisibilityChange(self, currentVisibleState):
##        '-no docstring-'
##        #return
##

class tagPALETTEENTRY(Structure):
    pass
tagLOGPALETTE._pack_ = 2.0
tagLOGPALETTE._fields_ = [
    ('palVersion', c_ushort),
    ('palNumEntries', c_ushort),
    ('palPalEntry', POINTER(tagPALETTEENTRY)),
]
assert sizeof(tagLOGPALETTE) == 8, sizeof(tagLOGPALETTE)
assert alignment(tagLOGPALETTE) == 2, alignment(tagLOGPALETTE)
IEnumFORMATETC._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagFORMATETC), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumFORMATETC)), 'ppenum' )),
]
################################################################
## code template for IEnumFORMATETC implementation
##class IEnumFORMATETC_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class AppShellVerbHandler(CoClass):
    _reg_clsid_ = GUID('{4ED3A719-CEA8-4BD9-910D-E252F997AFC2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IExecuteCommand(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7F9185B0-CB92-43C5-80A9-92277A4F7B54}')
    _idlflags_ = []
AppShellVerbHandler._com_interfaces_ = [IExecuteCommand]

tagPALETTEENTRY._fields_ = [
    ('peRed', c_ubyte),
    ('peGreen', c_ubyte),
    ('peBlue', c_ubyte),
    ('peFlags', c_ubyte),
]
assert sizeof(tagPALETTEENTRY) == 4, sizeof(tagPALETTEENTRY)
assert alignment(tagPALETTEENTRY) == 1, alignment(tagPALETTEENTRY)
_userFLAG_STGMEDIUM._fields_ = [
    ('ContextFlags', c_int),
    ('fPassOwnership', c_int),
    ('Stgmed', _userSTGMEDIUM),
]
assert sizeof(_userFLAG_STGMEDIUM) == 20, sizeof(_userFLAG_STGMEDIUM)
assert alignment(_userFLAG_STGMEDIUM) == 4, alignment(_userFLAG_STGMEDIUM)
IExecuteCommand._methods_ = [
    COMMETHOD([], HRESULT, 'SetKeyState',
              ( ['in'], c_ulong, 'grfKeyState' )),
    COMMETHOD([], HRESULT, 'SetParameters',
              ( ['in'], WSTRING, 'pszParameters' )),
    COMMETHOD([], HRESULT, 'SetPosition',
              ( ['in'], tagPOINT, 'pt' )),
    COMMETHOD([], HRESULT, 'SetShowWindow',
              ( ['in'], c_int, 'nShow' )),
    COMMETHOD([], HRESULT, 'SetNoShowUI',
              ( ['in'], c_int, 'fNoShowUI' )),
    COMMETHOD([], HRESULT, 'SetDirectory',
              ( ['in'], WSTRING, 'pszDirectory' )),
    COMMETHOD([], HRESULT, 'Execute'),
]
################################################################
## code template for IExecuteCommand implementation
##class IExecuteCommand_Impl(object):
##    def SetKeyState(self, grfKeyState):
##        '-no docstring-'
##        #return
##
##    def SetParameters(self, pszParameters):
##        '-no docstring-'
##        #return
##
##    def SetPosition(self, pt):
##        '-no docstring-'
##        #return
##
##    def SetShowWindow(self, nShow):
##        '-no docstring-'
##        #return
##
##    def SetNoShowUI(self, fNoShowUI):
##        '-no docstring-'
##        #return
##
##    def SetDirectory(self, pszDirectory):
##        '-no docstring-'
##        #return
##
##    def Execute(self):
##        '-no docstring-'
##        #return
##

class PackageDebugSettings(CoClass):
    _reg_clsid_ = GUID('{B1AEC16F-2383-4852-B0E9-8F0B1DC66B4D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IPackageDebugSettings(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F27C3930-8029-4AD1-94E3-3DBA417810C1}')
    _idlflags_ = []
class IPackageDebugSettings2(IPackageDebugSettings):
    _case_insensitive_ = True
    _iid_ = GUID('{6E3194BB-AB82-4D22-93F5-FABDA40E7B16}')
    _idlflags_ = []
PackageDebugSettings._com_interfaces_ = [IPackageDebugSettings2]


# values for enumeration 'SIATTRIBFLAGS'
SIATTRIBFLAGS_AND = 1
SIATTRIBFLAGS_OR = 2
SIATTRIBFLAGS_APPCOMPAT = 3
SIATTRIBFLAGS_MASK = 3
SIATTRIBFLAGS_ALLITEMS = 16384
SIATTRIBFLAGS = c_int # enum
class IEnumShellItems(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{70629033-E363-4A28-A567-0DB78006E6D7}')
    _idlflags_ = []
IShellItemArray._methods_ = [
    COMMETHOD([], HRESULT, 'BindToHandler',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(GUID), 'bhid' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppvOut' )),
    COMMETHOD([], HRESULT, 'GetPropertyStore',
              ( ['in'], GETPROPERTYSTOREFLAGS, 'Flags' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetPropertyDescriptionList',
              ( ['in'], POINTER(_tagpropertykey), 'keyType' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetAttributes',
              ( ['in'], SIATTRIBFLAGS, 'AttribFlags' ),
              ( ['in'], c_ulong, 'sfgaoMask' ),
              ( ['out'], POINTER(c_ulong), 'psfgaoAttribs' )),
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_ulong), 'pdwNumItems' )),
    COMMETHOD([], HRESULT, 'GetItemAt',
              ( ['in'], c_ulong, 'dwIndex' ),
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsi' )),
    COMMETHOD([], HRESULT, 'EnumItems',
              ( ['out'], POINTER(POINTER(IEnumShellItems)), 'ppenumShellItems' )),
]
################################################################
## code template for IShellItemArray implementation
##class IShellItemArray_Impl(object):
##    def BindToHandler(self, pbc, bhid, riid):
##        '-no docstring-'
##        #return ppvOut
##
##    def GetPropertyStore(self, Flags, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetPropertyDescriptionList(self, keyType, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetAttributes(self, AttribFlags, sfgaoMask):
##        '-no docstring-'
##        #return psfgaoAttribs
##
##    def GetCount(self):
##        '-no docstring-'
##        #return pdwNumItems
##
##    def GetItemAt(self, dwIndex):
##        '-no docstring-'
##        #return ppsi
##
##    def EnumItems(self):
##        '-no docstring-'
##        #return ppenumShellItems
##

class tagRemSNB(Structure):
    pass
wireSNB = POINTER(tagRemSNB)
tagRemSNB._fields_ = [
    ('ulCntStr', c_ulong),
    ('ulCntChar', c_ulong),
    ('rgString', POINTER(c_ushort)),
]
assert sizeof(tagRemSNB) == 12, sizeof(tagRemSNB)
assert alignment(tagRemSNB) == 4, alignment(tagRemSNB)
_FLAGGED_BYTE_BLOB._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('abData', POINTER(c_ubyte)),
]
assert sizeof(_FLAGGED_BYTE_BLOB) == 12, sizeof(_FLAGGED_BYTE_BLOB)
assert alignment(_FLAGGED_BYTE_BLOB) == 4, alignment(_FLAGGED_BYTE_BLOB)

# values for enumeration 'PACKAGE_EXECUTION_STATE'
PES_UNKNOWN = 0
PES_RUNNING = 1
PES_SUSPENDING = 2
PES_SUSPENDED = 3
PES_TERMINATED = 4
PACKAGE_EXECUTION_STATE = c_int # enum
class IPackageExecutionStateChangeNotification(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1BB12A62-2AD8-432B-8CCF-0C2C52AFCD5B}')
    _idlflags_ = []
IPackageDebugSettings._methods_ = [
    COMMETHOD([], HRESULT, 'EnableDebugging',
              ( ['in'], WSTRING, 'packageFullName' ),
              ( ['in'], WSTRING, 'debuggerCommandLine' ),
              ( ['in'], POINTER(c_ushort), 'environment' )),
    COMMETHOD([], HRESULT, 'DisableDebugging',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'Suspend',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'Resume',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'TerminateAllProcesses',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'SetTargetSessionId',
              ( ['in'], c_ulong, 'sessionId' )),
    COMMETHOD([], HRESULT, 'EnumerateBackgroundTasks',
              ( ['in'], WSTRING, 'packageFullName' ),
              ( ['out'], POINTER(c_ulong), 'taskCount' ),
              ( ['out'], POINTER(POINTER(GUID)), 'taskIds' ),
              ( ['out'], POINTER(POINTER(WSTRING)), 'taskNames' )),
    COMMETHOD([], HRESULT, 'ActivateBackgroundTask',
              ( ['in'], POINTER(GUID), 'taskId' )),
    COMMETHOD([], HRESULT, 'StartServicing',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'StopServicing',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'StartSessionRedirection',
              ( ['in'], WSTRING, 'packageFullName' ),
              ( ['in'], c_ulong, 'sessionId' )),
    COMMETHOD([], HRESULT, 'StopSessionRedirection',
              ( ['in'], WSTRING, 'packageFullName' )),
    COMMETHOD([], HRESULT, 'GetPackageExecutionState',
              ( ['in'], WSTRING, 'packageFullName' ),
              ( ['out'], POINTER(PACKAGE_EXECUTION_STATE), 'packageExecutionState' )),
    COMMETHOD([], HRESULT, 'RegisterForPackageStateChanges',
              ( ['in'], WSTRING, 'packageFullName' ),
              ( ['in'], POINTER(IPackageExecutionStateChangeNotification), 'pPackageExecutionStateChangeNotification' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'UnregisterForPackageStateChanges',
              ( ['in'], c_ulong, 'dwCookie' )),
]
################################################################
## code template for IPackageDebugSettings implementation
##class IPackageDebugSettings_Impl(object):
##    def EnableDebugging(self, packageFullName, debuggerCommandLine, environment):
##        '-no docstring-'
##        #return
##
##    def DisableDebugging(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def Suspend(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def Resume(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def TerminateAllProcesses(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def SetTargetSessionId(self, sessionId):
##        '-no docstring-'
##        #return
##
##    def EnumerateBackgroundTasks(self, packageFullName):
##        '-no docstring-'
##        #return taskCount, taskIds, taskNames
##
##    def ActivateBackgroundTask(self, taskId):
##        '-no docstring-'
##        #return
##
##    def StartServicing(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def StopServicing(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def StartSessionRedirection(self, packageFullName, sessionId):
##        '-no docstring-'
##        #return
##
##    def StopSessionRedirection(self, packageFullName):
##        '-no docstring-'
##        #return
##
##    def GetPackageExecutionState(self, packageFullName):
##        '-no docstring-'
##        #return packageExecutionState
##
##    def RegisterForPackageStateChanges(self, packageFullName, pPackageExecutionStateChangeNotification):
##        '-no docstring-'
##        #return pdwCookie
##
##    def UnregisterForPackageStateChanges(self, dwCookie):
##        '-no docstring-'
##        #return
##

class ExecuteUnknown(CoClass):
    _reg_clsid_ = GUID('{E44E9428-BDBC-4987-A099-40DC8FD255E7}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ExecuteUnknown._com_interfaces_ = [IExecuteCommand]

class IOperationsProgressDialog(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C9FB851-E5C9-43EB-A370-F0677B13874C}')
    _idlflags_ = []

# values for enumeration '_SPACTION'
SPACTION_NONE = 0
SPACTION_MOVING = 1
SPACTION_COPYING = 2
SPACTION_RECYCLING = 3
SPACTION_APPLYINGATTRIBS = 4
SPACTION_DOWNLOADING = 5
SPACTION_SEARCHING_INTERNET = 6
SPACTION_CALCULATING = 7
SPACTION_UPLOADING = 8
SPACTION_SEARCHING_FILES = 9
SPACTION_DELETING = 10
SPACTION_RENAMING = 11
SPACTION_FORMATTING = 12
SPACTION_COPY_MOVING = 13
_SPACTION = c_int # enum

# values for enumeration 'PDOPSTATUS'
PDOPS_RUNNING = 1
PDOPS_PAUSED = 2
PDOPS_CANCELLED = 3
PDOPS_STOPPED = 4
PDOPS_ERRORS = 5
PDOPSTATUS = c_int # enum
IOperationsProgressDialog._methods_ = [
    COMMETHOD([], HRESULT, 'StartProgressDialog',
              ( ['in'], wireHWND, 'hwndOwner' ),
              ( ['in'], c_ulong, 'Flags' )),
    COMMETHOD([], HRESULT, 'StopProgressDialog'),
    COMMETHOD([], HRESULT, 'SetOperation',
              ( ['in'], _SPACTION, 'action' )),
    COMMETHOD([], HRESULT, 'SetMode',
              ( ['in'], c_ulong, 'mode' )),
    COMMETHOD([], HRESULT, 'UpdateProgress',
              ( ['in'], c_ulonglong, 'ullPointsCurrent' ),
              ( ['in'], c_ulonglong, 'ullPointsTotal' ),
              ( ['in'], c_ulonglong, 'ullSizeCurrent' ),
              ( ['in'], c_ulonglong, 'ullSizeTotal' ),
              ( ['in'], c_ulonglong, 'ullItemsCurrent' ),
              ( ['in'], c_ulonglong, 'ullItemsTotal' )),
    COMMETHOD([], HRESULT, 'UpdateLocations',
              ( ['in'], POINTER(IShellItem), 'psiSource' ),
              ( ['in'], POINTER(IShellItem), 'psiTarget' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' )),
    COMMETHOD([], HRESULT, 'ResetTimer'),
    COMMETHOD([], HRESULT, 'PauseTimer'),
    COMMETHOD([], HRESULT, 'ResumeTimer'),
    COMMETHOD([], HRESULT, 'GetMilliseconds',
              ( ['out'], POINTER(c_ulonglong), 'pullElapsed' ),
              ( ['out'], POINTER(c_ulonglong), 'pullRemaining' )),
    COMMETHOD([], HRESULT, 'GetOperationStatus',
              ( ['out'], POINTER(PDOPSTATUS), 'popstatus' )),
]
################################################################
## code template for IOperationsProgressDialog implementation
##class IOperationsProgressDialog_Impl(object):
##    def StartProgressDialog(self, hwndOwner, Flags):
##        '-no docstring-'
##        #return
##
##    def StopProgressDialog(self):
##        '-no docstring-'
##        #return
##
##    def SetOperation(self, action):
##        '-no docstring-'
##        #return
##
##    def SetMode(self, mode):
##        '-no docstring-'
##        #return
##
##    def UpdateProgress(self, ullPointsCurrent, ullPointsTotal, ullSizeCurrent, ullSizeTotal, ullItemsCurrent, ullItemsTotal):
##        '-no docstring-'
##        #return
##
##    def UpdateLocations(self, psiSource, psiTarget, psiItem):
##        '-no docstring-'
##        #return
##
##    def ResetTimer(self):
##        '-no docstring-'
##        #return
##
##    def PauseTimer(self):
##        '-no docstring-'
##        #return
##
##    def ResumeTimer(self):
##        '-no docstring-'
##        #return
##
##    def GetMilliseconds(self):
##        '-no docstring-'
##        #return pullElapsed, pullRemaining
##
##    def GetOperationStatus(self):
##        '-no docstring-'
##        #return popstatus
##

IShellItemFilter._methods_ = [
    COMMETHOD([], HRESULT, 'IncludeItem',
              ( ['in'], POINTER(IShellItem), 'psi' )),
    COMMETHOD([], HRESULT, 'GetEnumFlagsForItem',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['out'], POINTER(c_ulong), 'pgrfFlags' )),
]
################################################################
## code template for IShellItemFilter implementation
##class IShellItemFilter_Impl(object):
##    def IncludeItem(self, psi):
##        '-no docstring-'
##        #return
##
##    def GetEnumFlagsForItem(self, psi):
##        '-no docstring-'
##        #return pgrfFlags
##

class EXTRASEARCH(Structure):
    pass
EXTRASEARCH._fields_ = [
    ('guidSearch', GUID),
    ('wszFriendlyName', c_ushort * 80),
    ('wszUrl', c_ushort * 2084),
]
assert sizeof(EXTRASEARCH) == 4344, sizeof(EXTRASEARCH)
assert alignment(EXTRASEARCH) == 4, alignment(EXTRASEARCH)
IPackageDebugSettings2._methods_ = [
    COMMETHOD([], HRESULT, 'EnumerateApps',
              ( ['in'], WSTRING, 'packageFullName' ),
              ( ['out'], POINTER(c_ulong), 'appCount' ),
              ( ['out'], POINTER(POINTER(WSTRING)), 'appUserModelIds' ),
              ( ['out'], POINTER(POINTER(WSTRING)), 'appDisplayNames' )),
]
################################################################
## code template for IPackageDebugSettings2 implementation
##class IPackageDebugSettings2_Impl(object):
##    def EnumerateApps(self, packageFullName):
##        '-no docstring-'
##        #return appCount, appUserModelIds, appDisplayNames
##

class ISuspensionDependencyManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{52B83A42-2543-416A-81D9-C0DE7969C8B3}')
    _idlflags_ = []
ISuspensionDependencyManager._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterAsChild',
              ( ['in'], c_void_p, 'processHandle' )),
    COMMETHOD([], HRESULT, 'GroupChildWithParent',
              ( ['in'], c_void_p, 'childProcessHandle' )),
    COMMETHOD([], HRESULT, 'UngroupChildFromParent',
              ( ['in'], c_void_p, 'childProcessHandle' )),
]
################################################################
## code template for ISuspensionDependencyManager implementation
##class ISuspensionDependencyManager_Impl(object):
##    def RegisterAsChild(self, processHandle):
##        '-no docstring-'
##        #return
##
##    def GroupChildWithParent(self, childProcessHandle):
##        '-no docstring-'
##        #return
##
##    def UngroupChildFromParent(self, childProcessHandle):
##        '-no docstring-'
##        #return
##

class INamespaceWalk(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{57CED8A7-3F4A-432C-9350-30F24483F74F}')
    _idlflags_ = []
INamespaceWalk._methods_ = [
    COMMETHOD([], HRESULT, 'Walk',
              ( ['in'], POINTER(IUnknown), 'punkToWalk' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_int, 'cDepth' ),
              ( ['in'], POINTER(INamespaceWalkCB), 'pnswcb' )),
    COMMETHOD([], HRESULT, 'GetIDArrayResult',
              ( ['out'], POINTER(c_uint), 'pcItems' ),
              ( ['out'], POINTER(POINTER(wirePIDL)), 'prgpidl' )),
]
################################################################
## code template for INamespaceWalk implementation
##class INamespaceWalk_Impl(object):
##    def Walk(self, punkToWalk, dwFlags, cDepth, pnswcb):
##        '-no docstring-'
##        #return
##
##    def GetIDArrayResult(self):
##        '-no docstring-'
##        #return pcItems, prgpidl
##

class NamespaceWalker(CoClass):
    _reg_clsid_ = GUID('{72EB61E0-8672-4303-9175-F2E4C68B2E7C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
NamespaceWalker._com_interfaces_ = [INamespaceWalk]

class FileSaveDialog(CoClass):
    _reg_clsid_ = GUID('{C0B4E2F3-BA21-4773-8DBA-335EC946EB8B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IFileSaveDialog(IFileDialog):
    _case_insensitive_ = True
    _iid_ = GUID('{84BCCD23-5FDE-4CDB-AEA4-AF64B83D78AB}')
    _idlflags_ = []
FileSaveDialog._com_interfaces_ = [IFileSaveDialog]

class SuspensionDependencyManager(CoClass):
    _reg_clsid_ = GUID('{6B273FC5-61FD-4918-95A2-C3B5E9D7F581}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
SuspensionDependencyManager._com_interfaces_ = [ISuspensionDependencyManager]

class IEnumSTATSTG(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000D-0000-0000-C000-000000000046}')
    _idlflags_ = []
IEnumSTATSTG._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagSTATSTG), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum' )),
]
################################################################
## code template for IEnumSTATSTG implementation
##class IEnumSTATSTG_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class FileOperation(CoClass):
    _reg_clsid_ = GUID('{3AD05575-8857-4850-9277-11B85BDB8E09}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
class IFileOperation(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{947AAB5F-0A5C-4C13-B4D6-4BF7836FC9F8}')
    _idlflags_ = []
FileOperation._com_interfaces_ = [IFileOperation]

IEnumShellItems._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(POINTER(IShellItem)), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumShellItems)), 'ppenum' )),
]
################################################################
## code template for IEnumShellItems implementation
##class IEnumShellItems_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class IFileOperationProgressSink(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{04B0F1A7-9490-44BC-96E1-4296A31252E2}')
    _idlflags_ = []
class IPropertyChangeArray(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{380F5CAD-1B5E-42F2-805D-637FD392D31E}')
    _idlflags_ = []
IFileOperation._methods_ = [
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IFileOperationProgressSink), 'pfops' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'SetOperationFlags',
              ( ['in'], c_ulong, 'dwOperationFlags' )),
    COMMETHOD([], HRESULT, 'SetProgressMessage',
              ( ['in'], WSTRING, 'pszMessage' )),
    COMMETHOD([], HRESULT, 'SetProgressDialog',
              ( ['in'], POINTER(IOperationsProgressDialog), 'popd' )),
    COMMETHOD([], HRESULT, 'SetProperties',
              ( ['in'], POINTER(IPropertyChangeArray), 'pproparray' )),
    COMMETHOD([], HRESULT, 'SetOwnerWindow',
              ( ['in'], wireHWND, 'hwndOwner' )),
    COMMETHOD([], HRESULT, 'ApplyPropertiesToItem',
              ( ['in'], POINTER(IShellItem), 'psiItem' )),
    COMMETHOD([], HRESULT, 'ApplyPropertiesToItems',
              ( ['in'], POINTER(IUnknown), 'punkItems' )),
    COMMETHOD([], HRESULT, 'RenameItem',
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], WSTRING, 'pszNewName' ),
              ( ['in'], POINTER(IFileOperationProgressSink), 'pfopsItem' )),
    COMMETHOD([], HRESULT, 'RenameItems',
              ( ['in'], POINTER(IUnknown), 'punkItems' ),
              ( ['in'], WSTRING, 'pszNewName' )),
    COMMETHOD([], HRESULT, 'MoveItem',
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' ),
              ( ['in'], POINTER(IFileOperationProgressSink), 'pfopsItem' )),
    COMMETHOD([], HRESULT, 'MoveItems',
              ( ['in'], POINTER(IUnknown), 'punkItems' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' )),
    COMMETHOD([], HRESULT, 'CopyItem',
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszCopyName' ),
              ( ['in'], POINTER(IFileOperationProgressSink), 'pfopsItem' )),
    COMMETHOD([], HRESULT, 'CopyItems',
              ( ['in'], POINTER(IUnknown), 'punkItems' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' )),
    COMMETHOD([], HRESULT, 'DeleteItem',
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IFileOperationProgressSink), 'pfopsItem' )),
    COMMETHOD([], HRESULT, 'DeleteItems',
              ( ['in'], POINTER(IUnknown), 'punkItems' )),
    COMMETHOD([], HRESULT, 'NewItem',
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], c_ulong, 'dwFileAttributes' ),
              ( ['in'], WSTRING, 'pszName' ),
              ( ['in'], WSTRING, 'pszTemplateName' ),
              ( ['in'], POINTER(IFileOperationProgressSink), 'pfopsItem' )),
    COMMETHOD([], HRESULT, 'PerformOperations'),
    COMMETHOD([], HRESULT, 'GetAnyOperationsAborted',
              ( ['out'], POINTER(c_int), 'pfAnyOperationsAborted' )),
]
################################################################
## code template for IFileOperation implementation
##class IFileOperation_Impl(object):
##    def Advise(self, pfops):
##        '-no docstring-'
##        #return pdwCookie
##
##    def Unadvise(self, dwCookie):
##        '-no docstring-'
##        #return
##
##    def SetOperationFlags(self, dwOperationFlags):
##        '-no docstring-'
##        #return
##
##    def SetProgressMessage(self, pszMessage):
##        '-no docstring-'
##        #return
##
##    def SetProgressDialog(self, popd):
##        '-no docstring-'
##        #return
##
##    def SetProperties(self, pproparray):
##        '-no docstring-'
##        #return
##
##    def SetOwnerWindow(self, hwndOwner):
##        '-no docstring-'
##        #return
##
##    def ApplyPropertiesToItem(self, psiItem):
##        '-no docstring-'
##        #return
##
##    def ApplyPropertiesToItems(self, punkItems):
##        '-no docstring-'
##        #return
##
##    def RenameItem(self, psiItem, pszNewName, pfopsItem):
##        '-no docstring-'
##        #return
##
##    def RenameItems(self, punkItems, pszNewName):
##        '-no docstring-'
##        #return
##
##    def MoveItem(self, psiItem, psiDestinationFolder, pszNewName, pfopsItem):
##        '-no docstring-'
##        #return
##
##    def MoveItems(self, punkItems, psiDestinationFolder):
##        '-no docstring-'
##        #return
##
##    def CopyItem(self, psiItem, psiDestinationFolder, pszCopyName, pfopsItem):
##        '-no docstring-'
##        #return
##
##    def CopyItems(self, punkItems, psiDestinationFolder):
##        '-no docstring-'
##        #return
##
##    def DeleteItem(self, psiItem, pfopsItem):
##        '-no docstring-'
##        #return
##
##    def DeleteItems(self, punkItems):
##        '-no docstring-'
##        #return
##
##    def NewItem(self, psiDestinationFolder, dwFileAttributes, pszName, pszTemplateName, pfopsItem):
##        '-no docstring-'
##        #return
##
##    def PerformOperations(self):
##        '-no docstring-'
##        #return
##
##    def GetAnyOperationsAborted(self):
##        '-no docstring-'
##        #return pfAnyOperationsAborted
##

_BYTE_BLOB._fields_ = [
    ('clSize', c_ulong),
    ('abData', POINTER(c_ubyte)),
]
assert sizeof(_BYTE_BLOB) == 8, sizeof(_BYTE_BLOB)
assert alignment(_BYTE_BLOB) == 4, alignment(_BYTE_BLOB)
class AppVisibility(CoClass):
    _reg_clsid_ = GUID('{7E5FE3D9-985F-4908-91F9-EE19F9FD1514}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
AppVisibility._com_interfaces_ = [IAppVisibility]

class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
assert sizeof(__MIDL_IWinTypes_0009) == 4, sizeof(__MIDL_IWinTypes_0009)
assert alignment(__MIDL_IWinTypes_0009) == 4, alignment(__MIDL_IWinTypes_0009)
_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
assert sizeof(_RemotableHandle) == 8, sizeof(_RemotableHandle)
assert alignment(_RemotableHandle) == 4, alignment(_RemotableHandle)
class IPropertyStore(IUnknown):
    _case_insensitive_ = True
    'Simple Property Store Interface'
    _iid_ = GUID('{886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99}')
    _idlflags_ = []
class IPropertyDescriptionList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1F9FC1D0-C39B-4B26-817F-011967D3440E}')
    _idlflags_ = []
IFileSaveDialog._methods_ = [
    COMMETHOD([], HRESULT, 'SetSaveAsItem',
              ( ['in'], POINTER(IShellItem), 'psi' )),
    COMMETHOD([], HRESULT, 'SetProperties',
              ( ['in'], POINTER(IPropertyStore), 'pStore' )),
    COMMETHOD([], HRESULT, 'SetCollectedProperties',
              ( ['in'], POINTER(IPropertyDescriptionList), 'pList' ),
              ( ['in'], c_int, 'fAppendDefault' )),
    COMMETHOD([], HRESULT, 'GetProperties',
              ( ['out'], POINTER(POINTER(IPropertyStore)), 'ppStore' )),
    COMMETHOD([], HRESULT, 'ApplyProperties',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], POINTER(IPropertyStore), 'pStore' ),
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(IFileOperationProgressSink), 'pSink' )),
]
################################################################
## code template for IFileSaveDialog implementation
##class IFileSaveDialog_Impl(object):
##    def SetSaveAsItem(self, psi):
##        '-no docstring-'
##        #return
##
##    def SetProperties(self, pStore):
##        '-no docstring-'
##        #return
##
##    def SetCollectedProperties(self, pList, fAppendDefault):
##        '-no docstring-'
##        #return
##
##    def GetProperties(self):
##        '-no docstring-'
##        #return ppStore
##
##    def ApplyProperties(self, psi, pStore, hwnd, pSink):
##        '-no docstring-'
##        #return
##

IStorage._methods_ = [
    COMMETHOD([], HRESULT, 'CreateStream',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
    COMMETHOD([], HRESULT, 'RemoteOpenStream',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'cbReserved1' ),
              ( ['in'], POINTER(c_ubyte), 'reserved1' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
    COMMETHOD([], HRESULT, 'CreateStorage',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStorage)), 'ppstg' )),
    COMMETHOD([], HRESULT, 'OpenStorage',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(IStorage), 'pstgPriority' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], wireSNB, 'snbExclude' ),
              ( ['in'], c_ulong, 'reserved' ),
              ( ['out'], POINTER(POINTER(IStorage)), 'ppstg' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], c_ulong, 'ciidExclude' ),
              ( ['in'], POINTER(GUID), 'rgiidExclude' ),
              ( ['in'], wireSNB, 'snbExclude' ),
              ( ['in'], POINTER(IStorage), 'pstgDest' )),
    COMMETHOD([], HRESULT, 'MoveElementTo',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(IStorage), 'pstgDest' ),
              ( ['in'], WSTRING, 'pwcsNewName' ),
              ( ['in'], c_ulong, 'grfFlags' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'RemoteEnumElements',
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'cbReserved2' ),
              ( ['in'], POINTER(c_ubyte), 'reserved2' ),
              ( ['in'], c_ulong, 'reserved3' ),
              ( ['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'DestroyElement',
              ( ['in'], WSTRING, 'pwcsName' )),
    COMMETHOD([], HRESULT, 'RenameElement',
              ( ['in'], WSTRING, 'pwcsOldName' ),
              ( ['in'], WSTRING, 'pwcsNewName' )),
    COMMETHOD([], HRESULT, 'SetElementTimes',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(_FILETIME), 'pctime' ),
              ( ['in'], POINTER(_FILETIME), 'patime' ),
              ( ['in'], POINTER(_FILETIME), 'pmtime' )),
    COMMETHOD([], HRESULT, 'SetClass',
              ( ['in'], POINTER(GUID), 'clsid' )),
    COMMETHOD([], HRESULT, 'SetStateBits',
              ( ['in'], c_ulong, 'grfStateBits' ),
              ( ['in'], c_ulong, 'grfMask' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
]
################################################################
## code template for IStorage implementation
##class IStorage_Impl(object):
##    def CreateStream(self, pwcsName, grfMode, reserved1, reserved2):
##        '-no docstring-'
##        #return ppstm
##
##    def RemoteOpenStream(self, pwcsName, cbReserved1, reserved1, grfMode, reserved2):
##        '-no docstring-'
##        #return ppstm
##
##    def CreateStorage(self, pwcsName, grfMode, reserved1, reserved2):
##        '-no docstring-'
##        #return ppstg
##
##    def OpenStorage(self, pwcsName, pstgPriority, grfMode, snbExclude, reserved):
##        '-no docstring-'
##        #return ppstg
##
##    def RemoteCopyTo(self, ciidExclude, rgiidExclude, snbExclude, pstgDest):
##        '-no docstring-'
##        #return
##
##    def MoveElementTo(self, pwcsName, pstgDest, pwcsNewName, grfFlags):
##        '-no docstring-'
##        #return
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return
##
##    def Revert(self):
##        '-no docstring-'
##        #return
##
##    def RemoteEnumElements(self, reserved1, cbReserved2, reserved2, reserved3):
##        '-no docstring-'
##        #return ppenum
##
##    def DestroyElement(self, pwcsName):
##        '-no docstring-'
##        #return
##
##    def RenameElement(self, pwcsOldName, pwcsNewName):
##        '-no docstring-'
##        #return
##
##    def SetElementTimes(self, pwcsName, pctime, patime, pmtime):
##        '-no docstring-'
##        #return
##
##    def SetClass(self, clsid):
##        '-no docstring-'
##        #return
##
##    def SetStateBits(self, grfStateBits, grfMask):
##        '-no docstring-'
##        #return
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##

class __MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001(Union):
    pass
__MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001._fields_ = [
    ('pOleStr', WSTRING),
    ('uOffset', c_uint),
    ('cStr', c_char * 260),
]
assert sizeof(__MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001) == 260, sizeof(__MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001)
assert alignment(__MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001) == 4, alignment(__MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001)
class _WIN32_FIND_DATAW(Structure):
    pass
_WIN32_FIND_DATAW._fields_ = [
    ('dwFileAttributes', c_ulong),
    ('ftCreationTime', _FILETIME),
    ('ftLastAccessTime', _FILETIME),
    ('ftLastWriteTime', _FILETIME),
    ('nFileSizeHigh', c_ulong),
    ('nFileSizeLow', c_ulong),
    ('dwReserved0', c_ulong),
    ('dwReserved1', c_ulong),
    ('cFileName', c_ushort * 260),
    ('cAlternateFileName', c_ushort * 14),
]
assert sizeof(_WIN32_FIND_DATAW) == 592, sizeof(_WIN32_FIND_DATAW)
assert alignment(_WIN32_FIND_DATAW) == 4, alignment(_WIN32_FIND_DATAW)
class IEnumExtraSearch(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0E700BE1-9DB6-11D1-A1CE-00C04FD75D13}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IEnumExtraSearch._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(EXTRASEARCH), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumExtraSearch)), 'ppenum' )),
]
################################################################
## code template for IEnumExtraSearch implementation
##class IEnumExtraSearch_Impl(object):
##    def Next(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

class IEnumIDList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{000214F2-0000-0000-C000-000000000046}')
    _idlflags_ = []
IEnumIDList._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(wirePIDL), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumIDList)), 'ppenum' )),
]
################################################################
## code template for IEnumIDList implementation
##class IEnumIDList_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##

wireASYNC_STGMEDIUM = POINTER(_userSTGMEDIUM)
IAdviseSink._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteOnDataChange',
              ( ['in'], POINTER(tagFORMATETC), 'pformatetc' ),
              ( ['in'], POINTER(wireASYNC_STGMEDIUM), 'pStgmed' )),
    COMMETHOD([], HRESULT, 'RemoteOnViewChange',
              ( ['in'], c_ulong, 'dwAspect' ),
              ( ['in'], c_int, 'lindex' )),
    COMMETHOD([], HRESULT, 'RemoteOnRename',
              ( ['in'], POINTER(IMoniker), 'pmk' )),
    COMMETHOD([], HRESULT, 'RemoteOnSave'),
    COMMETHOD([], HRESULT, 'RemoteOnClose'),
]
################################################################
## code template for IAdviseSink implementation
##class IAdviseSink_Impl(object):
##    def RemoteOnDataChange(self, pformatetc, pStgmed):
##        '-no docstring-'
##        #return
##
##    def RemoteOnViewChange(self, dwAspect, lindex):
##        '-no docstring-'
##        #return
##
##    def RemoteOnRename(self, pmk):
##        '-no docstring-'
##        #return
##
##    def RemoteOnSave(self):
##        '-no docstring-'
##        #return
##
##    def RemoteOnClose(self):
##        '-no docstring-'
##        #return
##

IPackageExecutionStateChangeNotification._methods_ = [
    COMMETHOD([], HRESULT, 'OnStateChanged',
              ( ['in'], WSTRING, 'pszPackageFullName' ),
              ( ['in'], PACKAGE_EXECUTION_STATE, 'pesNewState' )),
]
################################################################
## code template for IPackageExecutionStateChangeNotification implementation
##class IPackageExecutionStateChangeNotification_Impl(object):
##    def OnStateChanged(self, pszPackageFullName, pesNewState):
##        '-no docstring-'
##        #return
##

tagVersionedStream._fields_ = [
    ('guidVersion', GUID),
    ('pStream', POINTER(IStream)),
]
assert sizeof(tagVersionedStream) == 20, sizeof(tagVersionedStream)
assert alignment(tagVersionedStream) == 4, alignment(tagVersionedStream)
class _STRRET(Structure):
    pass
IShellFolder._methods_ = [
    COMMETHOD([], HRESULT, 'ParseDisplayName',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], WSTRING, 'pszDisplayName' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pchEaten' ),
              ( ['out'], POINTER(wirePIDL), 'ppidl' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwAttributes' )),
    COMMETHOD([], HRESULT, 'EnumObjects',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_ulong, 'grfFlags' ),
              ( ['out'], POINTER(POINTER(IEnumIDList)), 'ppenumIDList' )),
    COMMETHOD([], HRESULT, 'BindToObject',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'BindToStorage',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'CompareIDs',
              ( ['in'], LONG_PTR, 'lParam' ),
              ( ['in'], wirePIDL, 'pidl1' ),
              ( ['in'], wirePIDL, 'pidl2' )),
    COMMETHOD([], HRESULT, 'CreateViewObject',
              ( ['in'], wireHWND, 'hwndOwner' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetAttributesOf',
              ( ['in'], c_uint, 'cidl' ),
              ( ['in'], POINTER(wirePIDL), 'apidl' ),
              ( ['in', 'out'], POINTER(c_ulong), 'rgfInOut' )),
    COMMETHOD([], HRESULT, 'GetUIObjectOf',
              ( ['in'], wireHWND, 'hwndOwner' ),
              ( ['in'], c_uint, 'cidl' ),
              ( ['in'], POINTER(wirePIDL), 'apidl' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['in', 'out'], POINTER(c_uint), 'rgfReserved' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'GetDisplayNameOf',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], c_ulong, 'uFlags' ),
              ( ['out'], POINTER(_STRRET), 'pName' )),
    COMMETHOD([], HRESULT, 'RemoteSetNameOf',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], WSTRING, 'pszName' ),
              ( ['in'], c_ulong, 'uFlags' ),
              ( ['out'], POINTER(wirePIDL), 'ppidlOut' )),
]
################################################################
## code template for IShellFolder implementation
##class IShellFolder_Impl(object):
##    def ParseDisplayName(self, hwnd, pbc, pszDisplayName):
##        '-no docstring-'
##        #return pchEaten, ppidl, pdwAttributes
##
##    def EnumObjects(self, hwnd, grfFlags):
##        '-no docstring-'
##        #return ppenumIDList
##
##    def BindToObject(self, pidl, pbc, riid):
##        '-no docstring-'
##        #return ppv
##
##    def BindToStorage(self, pidl, pbc, riid):
##        '-no docstring-'
##        #return ppv
##
##    def CompareIDs(self, lParam, pidl1, pidl2):
##        '-no docstring-'
##        #return
##
##    def CreateViewObject(self, hwndOwner, riid):
##        '-no docstring-'
##        #return ppv
##
##    def GetAttributesOf(self, cidl, apidl):
##        '-no docstring-'
##        #return rgfInOut
##
##    def GetUIObjectOf(self, hwndOwner, cidl, apidl, riid):
##        '-no docstring-'
##        #return rgfReserved, ppv
##
##    def GetDisplayNameOf(self, pidl, uFlags):
##        '-no docstring-'
##        #return pName
##
##    def RemoteSetNameOf(self, hwnd, pidl, pszName, uFlags):
##        '-no docstring-'
##        #return ppidlOut
##

_STRRET._fields_ = [
    ('uType', c_uint),
    ('DUMMYUNIONNAME', __MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001),
]
assert sizeof(_STRRET) == 264, sizeof(_STRRET)
assert alignment(_STRRET) == 4, alignment(_STRRET)
tagCLIPDATA._fields_ = [
    ('cbSize', c_ulong),
    ('ulClipFmt', c_int),
    ('pClipData', POINTER(c_ubyte)),
]
assert sizeof(tagCLIPDATA) == 12, sizeof(tagCLIPDATA)
assert alignment(tagCLIPDATA) == 4, alignment(tagCLIPDATA)
IPropertyStore._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_ulong), 'cProps' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'iProp' ),
              ( ['out'], POINTER(_tagpropertykey), 'pkey' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'pv' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'propvar' )),
    COMMETHOD([], HRESULT, 'Commit'),
]
################################################################
## code template for IPropertyStore implementation
##class IPropertyStore_Impl(object):
##    def GetCount(self):
##        '-no docstring-'
##        #return cProps
##
##    def GetAt(self, iProp):
##        '-no docstring-'
##        #return pkey
##
##    def GetValue(self, key):
##        '-no docstring-'
##        #return pv
##
##    def SetValue(self, key, propvar):
##        '-no docstring-'
##        #return
##
##    def Commit(self):
##        '-no docstring-'
##        #return
##

IPropertyDescriptionList._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_uint), 'pcElem' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_uint, 'iElem' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
]
################################################################
## code template for IPropertyDescriptionList implementation
##class IPropertyDescriptionList_Impl(object):
##    def GetCount(self):
##        '-no docstring-'
##        #return pcElem
##
##    def GetAt(self, iElem, riid):
##        '-no docstring-'
##        #return ppv
##

class ShellDesktop(CoClass):
    _reg_clsid_ = GUID('{00021400-0000-0000-C000-000000000046}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ShellDesktop._com_interfaces_ = [IShellFolder2]

class EnumerableObjectCollection(CoClass):
    _reg_clsid_ = GUID('{2D3468C1-36A7-43B6-AC24-D3F02FD9607A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
EnumerableObjectCollection._com_interfaces_ = [IEnumObjects]

IFileOperationProgressSink._methods_ = [
    COMMETHOD([], HRESULT, 'StartOperations'),
    COMMETHOD([], HRESULT, 'FinishOperations',
              ( ['in'], HRESULT, 'hrResult' )),
    COMMETHOD([], HRESULT, 'PreRenameItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], WSTRING, 'pszNewName' )),
    COMMETHOD([], HRESULT, 'PostRenameItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], WSTRING, 'pszNewName' ),
              ( ['in'], HRESULT, 'hrRename' ),
              ( ['in'], POINTER(IShellItem), 'psiNewlyCreated' )),
    COMMETHOD([], HRESULT, 'PreMoveItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' )),
    COMMETHOD([], HRESULT, 'PostMoveItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' ),
              ( ['in'], HRESULT, 'hrMove' ),
              ( ['in'], POINTER(IShellItem), 'psiNewlyCreated' )),
    COMMETHOD([], HRESULT, 'PreCopyItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' )),
    COMMETHOD([], HRESULT, 'PostCopyItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' ),
              ( ['in'], HRESULT, 'hrCopy' ),
              ( ['in'], POINTER(IShellItem), 'psiNewlyCreated' )),
    COMMETHOD([], HRESULT, 'PreDeleteItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' )),
    COMMETHOD([], HRESULT, 'PostDeleteItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiItem' ),
              ( ['in'], HRESULT, 'hrDelete' ),
              ( ['in'], POINTER(IShellItem), 'psiNewlyCreated' )),
    COMMETHOD([], HRESULT, 'PreNewItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' )),
    COMMETHOD([], HRESULT, 'PostNewItem',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], POINTER(IShellItem), 'psiDestinationFolder' ),
              ( ['in'], WSTRING, 'pszNewName' ),
              ( ['in'], WSTRING, 'pszTemplateName' ),
              ( ['in'], c_ulong, 'dwFileAttributes' ),
              ( ['in'], HRESULT, 'hrNew' ),
              ( ['in'], POINTER(IShellItem), 'psiNewItem' )),
    COMMETHOD([], HRESULT, 'UpdateProgress',
              ( ['in'], c_uint, 'iWorkTotal' ),
              ( ['in'], c_uint, 'iWorkSoFar' )),
    COMMETHOD([], HRESULT, 'ResetTimer'),
    COMMETHOD([], HRESULT, 'PauseTimer'),
    COMMETHOD([], HRESULT, 'ResumeTimer'),
]
################################################################
## code template for IFileOperationProgressSink implementation
##class IFileOperationProgressSink_Impl(object):
##    def StartOperations(self):
##        '-no docstring-'
##        #return
##
##    def FinishOperations(self, hrResult):
##        '-no docstring-'
##        #return
##
##    def PreRenameItem(self, dwFlags, psiItem, pszNewName):
##        '-no docstring-'
##        #return
##
##    def PostRenameItem(self, dwFlags, psiItem, pszNewName, hrRename, psiNewlyCreated):
##        '-no docstring-'
##        #return
##
##    def PreMoveItem(self, dwFlags, psiItem, psiDestinationFolder, pszNewName):
##        '-no docstring-'
##        #return
##
##    def PostMoveItem(self, dwFlags, psiItem, psiDestinationFolder, pszNewName, hrMove, psiNewlyCreated):
##        '-no docstring-'
##        #return
##
##    def PreCopyItem(self, dwFlags, psiItem, psiDestinationFolder, pszNewName):
##        '-no docstring-'
##        #return
##
##    def PostCopyItem(self, dwFlags, psiItem, psiDestinationFolder, pszNewName, hrCopy, psiNewlyCreated):
##        '-no docstring-'
##        #return
##
##    def PreDeleteItem(self, dwFlags, psiItem):
##        '-no docstring-'
##        #return
##
##    def PostDeleteItem(self, dwFlags, psiItem, hrDelete, psiNewlyCreated):
##        '-no docstring-'
##        #return
##
##    def PreNewItem(self, dwFlags, psiDestinationFolder, pszNewName):
##        '-no docstring-'
##        #return
##
##    def PostNewItem(self, dwFlags, psiDestinationFolder, pszNewName, pszTemplateName, dwFileAttributes, hrNew, psiNewItem):
##        '-no docstring-'
##        #return
##
##    def UpdateProgress(self, iWorkTotal, iWorkSoFar):
##        '-no docstring-'
##        #return
##
##    def ResetTimer(self):
##        '-no docstring-'
##        #return
##
##    def PauseTimer(self):
##        '-no docstring-'
##        #return
##
##    def ResumeTimer(self):
##        '-no docstring-'
##        #return
##

IPropertyChangeArray._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_uint), 'pcOperations' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_uint, 'iIndex' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'InsertAt',
              ( ['in'], c_uint, 'iIndex' ),
              ( ['in'], POINTER(IPropertyChange), 'ppropChange' )),
    COMMETHOD([], HRESULT, 'Append',
              ( ['in'], POINTER(IPropertyChange), 'ppropChange' )),
    COMMETHOD([], HRESULT, 'AppendOrReplace',
              ( ['in'], POINTER(IPropertyChange), 'ppropChange' )),
    COMMETHOD([], HRESULT, 'RemoveAt',
              ( ['in'], c_uint, 'iIndex' )),
    COMMETHOD([], HRESULT, 'IsKeyInArray',
              ( ['in'], POINTER(_tagpropertykey), 'key' )),
]
################################################################
## code template for IPropertyChangeArray implementation
##class IPropertyChangeArray_Impl(object):
##    def GetCount(self):
##        '-no docstring-'
##        #return pcOperations
##
##    def GetAt(self, iIndex, riid):
##        '-no docstring-'
##        #return ppv
##
##    def InsertAt(self, iIndex, ppropChange):
##        '-no docstring-'
##        #return
##
##    def Append(self, ppropChange):
##        '-no docstring-'
##        #return
##
##    def AppendOrReplace(self, ppropChange):
##        '-no docstring-'
##        #return
##
##    def RemoveAt(self, iIndex):
##        '-no docstring-'
##        #return
##
##    def IsKeyInArray(self, key):
##        '-no docstring-'
##        #return
##

IShellLinkW._methods_ = [
    COMMETHOD([], HRESULT, 'GetPath',
              ( ['out'], WSTRING, 'pszFile' ),
              ( ['in'], c_int, 'cch' ),
              ( ['in', 'out'], POINTER(_WIN32_FIND_DATAW), 'pfd' ),
              ( ['in'], c_ulong, 'fFlags' )),
    COMMETHOD([], HRESULT, 'GetIDList',
              ( ['out'], POINTER(wirePIDL), 'ppidl' )),
    COMMETHOD([], HRESULT, 'SetIDList',
              ( ['in'], wirePIDL, 'pidl' )),
    COMMETHOD([], HRESULT, 'GetDescription',
              ( ['out'], WSTRING, 'pszName' ),
              ( [], c_int, 'cch' )),
    COMMETHOD([], HRESULT, 'SetDescription',
              ( ['in'], WSTRING, 'pszName' )),
    COMMETHOD([], HRESULT, 'GetWorkingDirectory',
              ( ['out'], WSTRING, 'pszDir' ),
              ( [], c_int, 'cch' )),
    COMMETHOD([], HRESULT, 'SetWorkingDirectory',
              ( ['in'], WSTRING, 'pszDir' )),
    COMMETHOD([], HRESULT, 'GetArguments',
              ( ['out'], WSTRING, 'pszArgs' ),
              ( ['in'], c_int, 'cch' )),
    COMMETHOD([], HRESULT, 'SetArguments',
              ( ['in'], WSTRING, 'pszArgs' )),
    COMMETHOD([], HRESULT, 'GetHotkey',
              ( ['out'], POINTER(c_ushort), 'pwHotkey' )),
    COMMETHOD([], HRESULT, 'SetHotkey',
              ( ['in'], c_ushort, 'wHotkey' )),
    COMMETHOD([], HRESULT, 'GetShowCmd',
              ( ['out'], POINTER(c_int), 'piShowCmd' )),
    COMMETHOD([], HRESULT, 'SetShowCmd',
              ( ['in'], c_int, 'iShowCmd' )),
    COMMETHOD([], HRESULT, 'GetIconLocation',
              ( ['out'], WSTRING, 'pszIconPath' ),
              ( ['in'], c_int, 'cch' ),
              ( ['out'], POINTER(c_int), 'piIcon' )),
    COMMETHOD([], HRESULT, 'SetIconLocation',
              ( ['in'], WSTRING, 'pszIconPath' ),
              ( ['in'], c_int, 'iIcon' )),
    COMMETHOD([], HRESULT, 'SetRelativePath',
              ( ['in'], WSTRING, 'pszPathRel' ),
              ( ['in'], c_ulong, 'dwReserved' )),
    COMMETHOD([], HRESULT, 'Resolve',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], c_ulong, 'fFlags' )),
    COMMETHOD([], HRESULT, 'SetPath',
              ( ['in'], WSTRING, 'pszFile' )),
]
################################################################
## code template for IShellLinkW implementation
##class IShellLinkW_Impl(object):
##    def GetPath(self, cch, fFlags):
##        '-no docstring-'
##        #return pszFile, pfd
##
##    def GetIDList(self):
##        '-no docstring-'
##        #return ppidl
##
##    def SetIDList(self, pidl):
##        '-no docstring-'
##        #return
##
##    def GetDescription(self, cch):
##        '-no docstring-'
##        #return pszName
##
##    def SetDescription(self, pszName):
##        '-no docstring-'
##        #return
##
##    def GetWorkingDirectory(self, cch):
##        '-no docstring-'
##        #return pszDir
##
##    def SetWorkingDirectory(self, pszDir):
##        '-no docstring-'
##        #return
##
##    def GetArguments(self, cch):
##        '-no docstring-'
##        #return pszArgs
##
##    def SetArguments(self, pszArgs):
##        '-no docstring-'
##        #return
##
##    def GetHotkey(self):
##        '-no docstring-'
##        #return pwHotkey
##
##    def SetHotkey(self, wHotkey):
##        '-no docstring-'
##        #return
##
##    def GetShowCmd(self):
##        '-no docstring-'
##        #return piShowCmd
##
##    def SetShowCmd(self, iShowCmd):
##        '-no docstring-'
##        #return
##
##    def GetIconLocation(self, cch):
##        '-no docstring-'
##        #return pszIconPath, piIcon
##
##    def SetIconLocation(self, pszIconPath, iIcon):
##        '-no docstring-'
##        #return
##
##    def SetRelativePath(self, pszPathRel, dwReserved):
##        '-no docstring-'
##        #return
##
##    def Resolve(self, hwnd, fFlags):
##        '-no docstring-'
##        #return
##
##    def SetPath(self, pszFile):
##        '-no docstring-'
##        #return
##

class __MIDL_IOleAutomationTypes_0005(Union):
    pass
__MIDL_IOleAutomationTypes_0005._fields_ = [
    ('lptdesc', POINTER(tagTYPEDESC)),
    ('lpadesc', POINTER(tagARRAYDESC)),
    ('hreftype', c_ulong),
]
assert sizeof(__MIDL_IOleAutomationTypes_0005) == 4, sizeof(__MIDL_IOleAutomationTypes_0005)
assert alignment(__MIDL_IOleAutomationTypes_0005) == 4, alignment(__MIDL_IOleAutomationTypes_0005)
class tagSTATDATA(Structure):
    pass
IEnumSTATDATA._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagSTATDATA), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumSTATDATA)), 'ppenum' )),
]
################################################################
## code template for IEnumSTATDATA implementation
##class IEnumSTATDATA_Impl(object):
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##


# values for enumeration 'APPLICATION_VIEW_MIN_WIDTH'
AVMW_DEFAULT = 0
AVMW_320 = 1
AVMW_500 = 2
APPLICATION_VIEW_MIN_WIDTH = c_int # enum
class ShellFSFolder(CoClass):
    _reg_clsid_ = GUID('{F3364BA0-65B9-11CE-A9BA-00AA004AE837}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ShellFSFolder._com_interfaces_ = [IShellFolder2]

class _SHELLDETAILS(Structure):
    pass
_SHELLDETAILS._fields_ = [
    ('fmt', c_int),
    ('cxChar', c_int),
    ('str', _STRRET),
]
assert sizeof(_SHELLDETAILS) == 272, sizeof(_SHELLDETAILS)
assert alignment(_SHELLDETAILS) == 4, alignment(_SHELLDETAILS)
class NetworkPlaces(CoClass):
    _reg_clsid_ = GUID('{208D2C60-3AEA-1069-A2D7-08002B30309D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
NetworkPlaces._com_interfaces_ = [IShellFolder2]

IShellFolder2._methods_ = [
    COMMETHOD([], HRESULT, 'GetDefaultSearchGUID',
              ( ['out'], POINTER(GUID), 'pguid' )),
    COMMETHOD([], HRESULT, 'EnumSearches',
              ( ['out'], POINTER(POINTER(IEnumExtraSearch)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'GetDefaultColumn',
              ( ['in'], c_ulong, 'dwRes' ),
              ( ['out'], POINTER(c_ulong), 'pSort' ),
              ( ['out'], POINTER(c_ulong), 'pDisplay' )),
    COMMETHOD([], HRESULT, 'GetDefaultColumnState',
              ( ['in'], c_uint, 'iColumn' ),
              ( ['out'], POINTER(c_ulong), 'pcsFlags' )),
    COMMETHOD([], HRESULT, 'GetDetailsEx',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], POINTER(_tagpropertykey), 'pscid' ),
              ( ['out'], POINTER(VARIANT), 'pv' )),
    COMMETHOD([], HRESULT, 'GetDetailsOf',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], c_uint, 'iColumn' ),
              ( ['out'], POINTER(_SHELLDETAILS), 'psd' )),
    COMMETHOD([], HRESULT, 'MapColumnToSCID',
              ( ['in'], c_uint, 'iColumn' ),
              ( ['out'], POINTER(_tagpropertykey), 'pscid' )),
]
################################################################
## code template for IShellFolder2 implementation
##class IShellFolder2_Impl(object):
##    def GetDefaultSearchGUID(self):
##        '-no docstring-'
##        #return pguid
##
##    def EnumSearches(self):
##        '-no docstring-'
##        #return ppenum
##
##    def GetDefaultColumn(self, dwRes):
##        '-no docstring-'
##        #return pSort, pDisplay
##
##    def GetDefaultColumnState(self, iColumn):
##        '-no docstring-'
##        #return pcsFlags
##
##    def GetDetailsEx(self, pidl, pscid):
##        '-no docstring-'
##        #return pv
##
##    def GetDetailsOf(self, pidl, iColumn):
##        '-no docstring-'
##        #return psd
##
##    def MapColumnToSCID(self, iColumn):
##        '-no docstring-'
##        #return pscid
##

IFrameworkInputPaneHandler._methods_ = [
    COMMETHOD([], HRESULT, 'Showing',
              ( ['in'], POINTER(tagRECT), 'prcInputPaneScreenLocation' ),
              ( ['in'], c_int, 'fEnsureFocusedElementInView' )),
    COMMETHOD([], HRESULT, 'Hiding',
              ( ['in'], c_int, 'fEnsureFocusedElementInView' )),
]
################################################################
## code template for IFrameworkInputPaneHandler implementation
##class IFrameworkInputPaneHandler_Impl(object):
##    def Showing(self, prcInputPaneScreenLocation, fEnsureFocusedElementInView):
##        '-no docstring-'
##        #return
##
##    def Hiding(self, fEnsureFocusedElementInView):
##        '-no docstring-'
##        #return
##

_wireSAFEARRAY._fields_ = [
    ('cDims', c_ushort),
    ('fFeatures', c_ushort),
    ('cbElements', c_ulong),
    ('cLocks', c_ulong),
    ('uArrayStructs', _wireSAFEARRAY_UNION),
    ('rgsabound', POINTER(tagSAFEARRAYBOUND)),
]
assert sizeof(_wireSAFEARRAY) == 44, sizeof(_wireSAFEARRAY)
assert alignment(_wireSAFEARRAY) == 4, alignment(_wireSAFEARRAY)
class ApplicationActivationManager(CoClass):
    _reg_clsid_ = GUID('{45BA127D-10A8-46EA-8AB7-56EA9078943C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ApplicationActivationManager._com_interfaces_ = [IApplicationActivationManager]

class ShellLink(CoClass):
    _reg_clsid_ = GUID('{00021401-0000-0000-C000-000000000046}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{56F9F44F-F74C-4E38-99BC-9F3EBD3D696A}', 1, 0)
ShellLink._com_interfaces_ = [IShellLinkW]

tagSTATDATA._fields_ = [
    ('formatetc', tagFORMATETC),
    ('advf', c_ulong),
    ('pAdvSink', POINTER(IAdviseSink)),
    ('dwConnection', c_ulong),
]
assert sizeof(tagSTATDATA) == 32, sizeof(tagSTATDATA)
assert alignment(tagSTATDATA) == 4, alignment(tagSTATDATA)
IApplicationDesignModeSettings2._methods_ = [
    COMMETHOD([], HRESULT, 'SetNativeDisplayOrientation',
              ( ['in'], NATIVE_DISPLAY_ORIENTATION, 'nativeDisplayOrientation' )),
    COMMETHOD([], HRESULT, 'SetApplicationViewOrientation',
              ( ['in'], APPLICATION_VIEW_ORIENTATION, 'viewOrientation' )),
    COMMETHOD([], HRESULT, 'SetAdjacentDisplayEdges',
              ( ['in'], ADJACENT_DISPLAY_EDGES, 'adjacentDisplayEdges' )),
    COMMETHOD([], HRESULT, 'SetIsOnLockScreen',
              ( ['in'], c_int, 'isOnLockScreen' )),
    COMMETHOD([], HRESULT, 'SetApplicationViewMinWidth',
              ( ['in'], APPLICATION_VIEW_MIN_WIDTH, 'viewMinWidth' )),
    COMMETHOD([], HRESULT, 'GetApplicationSizeBounds',
              ( ['out'], POINTER(tagSIZE), 'minApplicationSizePixels' ),
              ( ['out'], POINTER(tagSIZE), 'maxApplicationSizePixels' )),
    COMMETHOD([], HRESULT, 'GetApplicationViewOrientation',
              ( ['in'], tagSIZE, 'applicationSizePixels' ),
              ( ['out'], POINTER(APPLICATION_VIEW_ORIENTATION), 'viewOrientation' )),
]
################################################################
## code template for IApplicationDesignModeSettings2 implementation
##class IApplicationDesignModeSettings2_Impl(object):
##    def SetNativeDisplayOrientation(self, nativeDisplayOrientation):
##        '-no docstring-'
##        #return
##
##    def SetApplicationViewOrientation(self, viewOrientation):
##        '-no docstring-'
##        #return
##
##    def SetAdjacentDisplayEdges(self, adjacentDisplayEdges):
##        '-no docstring-'
##        #return
##
##    def SetIsOnLockScreen(self, isOnLockScreen):
##        '-no docstring-'
##        #return
##
##    def SetApplicationViewMinWidth(self, viewMinWidth):
##        '-no docstring-'
##        #return
##
##    def GetApplicationSizeBounds(self):
##        '-no docstring-'
##        #return minApplicationSizePixels, maxApplicationSizePixels
##
##    def GetApplicationViewOrientation(self, applicationSizePixels):
##        '-no docstring-'
##        #return viewOrientation
##

__all__ = [ 'DSS_DISABLED_BY_REMOTE_SESSION', 'SCALE_180_PERCENT',
           'COP_WORD_STARTSWITH', 'tagBLOB', 'SIATTRIBFLAGS_ALLITEMS',
           'TBPF_INDETERMINATE', 'IEnumMoniker', 'IEnumSTATDATA',
           'tagCLIPDATA', 'tagCAUI', 'FLVM_TILES', '_HYPER_SIZEDARR',
           'DWPOS_FIT', 'DFMR_NO_RESOURCE_VERBS', 'LFF_ALLITEMS',
           'IShellItem', 'IEnumString', 'LONG_PTR', '_BYTE_SIZEDARR',
           'ISharingConfigurationManager', 'IFileDialog',
           '_wireSAFEARRAY_UNION', 'SPACTION_COPYING', '_SPACTION',
           'MAV_UNKNOWN', 'DSFT_DETECT', 'ADE_LEFT', 'GPS_TEMPORARY',
           '_userBITMAP', 'AVS_FULLSCREEN_LANDSCAPE',
           'SPACTION_CALCULATING', '_STRRET', 'tagCADBL', 'wirePIDL',
           '_wireSAFEARRAY', 'ITaskbarList4', 'PDOPSTATUS',
           'ACTIVATEOPTIONS', 'CPVIEW', '_FLAGGED_WORD_BLOB',
           'IShellLinkW', 'SIATTRIBFLAGS_APPCOMPAT', 'tagRemSNB',
           'GPS_HANDLERPROPERTIESONLY', 'tagSTATDATA',
           '_wireSAFEARR_VARIANT', 'tagCONDITION_TYPE',
           'LIBRARYFOLDERFILTER', '_userHMETAFILE',
           'MAV_NO_APP_VISIBLE', 'SPACTION_MOVING',
           'IApplicationDestinations', 'wireHMONITOR',
           'DefFolderMenu', '_COMDLG_FILTERSPEC', 'CPVIEW_CLASSIC',
           'IStorage', 'IEnumIDList', 'FDESVR_ACCEPT', 'ICondition',
           'TBPF_ERROR', 'IStream', 'PDOPS_PAUSED', 'CATSORT_DEFAULT',
           'STPF_USEAPPPEEKALWAYS', 'KDC_FREQUENT',
           'SCALE_125_PERCENT', 'AVO_PORTRAIT',
           'ApplicationDesignModeSettings', 'IRichChunk',
           'FDESVR_DEFAULT', 'THB_BITMAP', 'IEnumSTATSTG',
           'tagCABSTRBLOB', 'IObjectWithPropertyKey',
           'tagCONDITION_OPERATION', 'DWPOS_FILL', 'AT_FILEEXTENSION',
           'SIGDN_DESKTOPABSOLUTEEDITING', 'IAdviseSink',
           '__MIDL_IWinTypes_0005', 'DFMR_NO_ASYNC_VERBS',
           'GPS_NO_OPLOCK', 'CATINFO_NOTCOLLAPSIBLE',
           'SIGDN_PARENTRELATIVEPARSING', 'AO_DESIGNMODE',
           'tagSTATSTG', 'IShellFolder2', 'AppStartupLink',
           'IFileSaveDialog', 'AVS_SNAPPED', 'LIBRARYOPTIONFLAGS',
           '__MIDL_IOleAutomationTypes_0005', 'INamespaceWalkCB',
           'AO_NONE', 'IApplicationDesignModeSettings', 'ShellItem',
           'IShellFolder', '__MIDL_IWinTypes_0006',
           '__MIDL_IWinTypes_0001', 'IEnumExtraSearch', 'FLVM_LAST',
           'DFMR_NO_STATIC_VERBS', 'SharingConfigurationManager',
           '_BYTE_BLOB', 'NetworkExplorerFolder', 'wireCLIPFORMAT',
           'FOLDERLOGICALVIEWMODE', 'THBF_DISMISSONCLICK',
           'CT_LEAF_CONDITION', 'DEFSHAREID_USERS',
           'KF_CATEGORY_FIXED', '__MIDL_IOleAutomationTypes_0006',
           'SIGDN_NORMALDISPLAY', 'PES_UNKNOWN', 'HGSC_PRINTERS',
           '_userHPALETTE', '_GDI_OBJECT', 'IOpenControlPanel',
           'GETPROPERTYSTOREFLAGS', 'AO_NOERRORUI',
           '_wireSAFEARR_DISPATCH', 'ExecuteUnknown',
           'IShellItemFilter', 'tagCAUB', 'tagCACLIPDATA', 'IMoniker',
           'IShellLibrary', 'tagCAI', 'THUMBBUTTONFLAGS',
           'IModalWindow', 'tagCABOOL', 'TaskbarList', 'LOF_DEFAULT',
           'SearchFolderItemFactory', 'SCALE_175_PERCENT',
           'THBF_ENABLED', 'SIGDN_URL', 'GPS_DELAYCREATION',
           'TBPF_NOPROGRESS', 'IDesktopWallpaper', 'GPS_DEFAULT',
           'wireFLAG_STGMEDIUM', 'DEFAULTSAVEFOLDERTYPE',
           'IAppVisibility', 'ASSOCIATIONTYPE',
           'FreeSpaceCategorizer', 'tagCAL', 'LSF_FAILIFTHERE',
           'SCALE_400_PERCENT', 'SCALE_300_PERCENT',
           'SCALE_150_PERCENT', 'tagCALPWSTR',
           '__MIDL_IAdviseSink_0003', 'THB_ICON', 'DFMR_DEFAULT',
           'ICategorizer', 'CATEGORYINFO_FLAGS', 'tagCAUL',
           'COP_APPLICATION_SPECIFIC', 'SHARE_ROLE_INVALID',
           'DEF_SHARE_ID', 'ADLT_FREQUENT', 'wireSNB',
           '__MIDL_IOleAutomationTypes_0004', '__MIDL_IWinTypes_0004',
           'EXTRASEARCH', 'SHARE_ROLE_CO_OWNER',
           'ISearchFolderItemFactory', 'THB_FLAGS',
           'DFMR_USE_SPECIFIED_VERBS', 'SCALE_225_PERCENT',
           'STPF_USEAPPPEEKWHENACTIVE', 'IKnownFolderManager',
           'SCALE_160_PERCENT', 'SIGDN_PARENTRELATIVEFORUI',
           'FFFP_MODE', 'tagBSTRBLOB',
           'SIGDN_PARENTRELATIVEFORADDRESSBAR', 'AO_NOSPLASHSCREEN',
           'NATIVE_DISPLAY_ORIENTATION',
           'SPACTION_SEARCHING_INTERNET', 'tagCAFLT', 'wireSTGMEDIUM',
           'SCALE_140_PERCENT', 'IFileOperation', 'DSS_SLIDESHOW',
           'CPVIEW_ALLITEMS', 'SHARE_ROLE_READER',
           'SCALE_250_PERCENT', 'COP_LESSTHANOREQUAL', 'HomeGroup',
           'ApplicationActivationManager', '_SIGDN', 'GPS_BESTEFFORT',
           'COP_WORD_EQUAL', 'ISequentialStream',
           'COP_GREATERTHANOREQUAL', 'KF_CATEGORY_COMMON',
           'DestinationList', 'DESKTOP_SLIDESHOW_DIRECTION',
           'APPLICATION_VIEW_ORIENTATION', 'AO_PRELAUNCH',
           'CT_AND_CONDITION', 'IAppVisibilityEvents',
           '__MIDL_IOleAutomationTypes_0001',
           'IDefaultFolderMenuInitialize', 'FDAP', 'CPVIEW_HOME',
           'DSFT_PUBLIC', 'IPropertyUI', 'SCALE_200_PERCENT',
           'GPS_READWRITE', 'AL_EFFECTIVE', 'SCALE_120_PERCENT',
           'FDAP_TOP', 'SPACTION_NONE', 'SPACTION_COPY_MOVING',
           'IShellItem2', 'GPS_OPENSLOWITEM',
           'GPS_FASTPROPERTIESONLY', 'SuspensionDependencyManager',
           'COP_EQUAL', 'FileSaveDialog', 'SIGDN_FILESYSPATH',
           'NDO_LANDSCAPE', '_SHELLDETAILS', 'KF_CATEGORY_VIRTUAL',
           'SIGDN_DESKTOPABSOLUTEPARSING',
           'ApplicationAssociationRegistration', 'SCALE_450_PERCENT',
           'AT_URLPROTOCOL', 'IPackageDebugSettings',
           'SIGDN_PARENTRELATIVEEDITING', 'AVO_LANDSCAPE',
           'SPACTION_RECYCLING', 'IHomeGroup', 'COP_VALUE_STARTSWITH',
           'COP_VALUE_NOTCONTAINS', 'AL_USER', '_userSTGMEDIUM',
           'ISuspensionDependencyManager', 'ShellLibrary',
           'MailRecipient', 'DFMR_OPTIN_HANDLERS_ONLY',
           'tagCAFILETIME', 'IDataObject', 'PES_SUSPENDED',
           'LSF_MAKEUNIQUENAME', 'GPS_EXTRINSICPROPERTIESONLY',
           'DSD_FORWARD', 'FLVM_UNSPECIFIED', '_wireVARIANT',
           'THBF_DISABLED', 'APPLICATION_VIEW_MIN_WIDTH',
           'PDOPS_RUNNING', 'SIATTRIBFLAGS_MASK', 'CATSORT_NAME',
           'DEFSHAREID_PUBLIC', 'IBindCtx', 'SCALE_100_PERCENT',
           'DFMR_STATIC_VERBS_ONLY', 'PropertiesUI', 'ScheduledTasks',
           'SIATTRIBFLAGS_AND', 'FFFP_NEARESTPARENTMATCH',
           'COP_DOSWILDCARDS', 'HOMEGROUPSHARINGCHOICES',
           'CATEGORY_INFO', '__MIDL_IWinTypes_0007',
           '_userHENHMETAFILE', 'FDE_OVERWRITE_RESPONSE',
           'SCALE_500_PERCENT', 'IObjectArray', 'FLVM_LIST',
           'GPS_MASK_VALID', 'NetworkConnections',
           'SPACTION_UPLOADING', 'IRunningObjectTable',
           'PDOPS_STOPPED', 'IPackageDebugSettings2', 'HGSC_NONE',
           'COP_NOTEQUAL', 'MONITOR_APP_VISIBILITY', 'FDESVR_REFUSE',
           'SPACTION_FORMATTING', 'SIATTRIBFLAGS', 'ShellDesktop',
           'AVMW_320', 'ITaskbarList2', '__MIDL_IWinTypes_0009',
           'tag_inner_PROPVARIANT', 'CATINFO_NOHEADER',
           'FrameworkInputPane', 'AVS_FILLED', 'DSD_BACKWARD',
           'FDEOR_REFUSE', '_userCLIPFORMAT',
           'CATINFO_SEPARATE_IMAGES', 'ADE_NONE', 'LIBRARYSAVEFLAGS',
           'DEVICE_SCALE_FACTOR', 'LFF_STORAGEITEMS',
           '__MIDL___MIDL_itf_ShObjIdl_core_0001_0091_0001',
           'SCALE_350_PERCENT', 'IFrameworkInputPaneHandler',
           'SORTCOLUMN', 'PackageDebugSettings', 'ITaskbarList',
           'IPropertyChange', 'tagVersionedStream', 'IPersistStream',
           'DSS_ENABLED', 'SPACTION_RENAMING', 'SHARE_ROLE',
           'DriveSizeCategorizer', 'AppVisibility', 'TBPF_PAUSED',
           'DWPOS_CENTER', 'SizeCategorizer', 'COP_IMPLICIT',
           'IOperationsProgressDialog', 'KNOWNDESTCATEGORY',
           'DESKTOP_WALLPAPER_POSITION',
           'DFMR_USE_SPECIFIED_HANDLERS',
           'IApplicationAssociationRegistration', 'TBPF_NORMAL',
           'FLVM_DETAILS', 'CATINFO_NOHEADERCOUNT', 'LOF_MASK_ALL',
           'IFileDialogEvents', 'tagCAUH', 'THBF_NONINTERACTIVE',
           'FLVM_FIRST', 'EGK_MOUSE', '_wireSAFEARR_UNKNOWN',
           '_tagpropertykey', 'CPVIEW_CATEGORY', 'FileOperation',
           '_SHORT_SIZEDARR', 'tagFORMATETC', 'FDEOR_ACCEPT',
           'IFileOperationProgressSink',
           'IApplicationDesignModeSettings2', 'tagCACLSID',
           'GPS_PREFERQUERYPROPERTIES', 'ITaskbarList3',
           'CATINFO_HIDDEN', 'tagCAC', '_LONG_SIZEDARR',
           'HGSC_DOCUMENTSLIBRARY', 'IApplicationDocumentLists',
           'IUserNotification', 'DSFT_PRIVATE', 'UINT_PTR',
           'EGK_TOUCH', 'MAV_APP_VISIBLE', '_wireBRECORD',
           '_remoteMETAFILEPICT', '_userHBITMAP', 'ADLT_RECENT',
           'tagCASCODE', 'NamespaceWalker', 'IPropertyChangeArray',
           'SPACTION_SEARCHING_FILES', 'COP_GREATERTHAN',
           'AT_STARTMENUCLIENT', 'LFF_FORCEFILESYSTEM',
           'THUMBBUTTONMASK', 'DESKTOP_SLIDESHOW_STATE',
           'IExecuteCommand', 'AppShellVerbHandler', 'FileOpenDialog',
           'SPACTION_DELETING', '_FLAGGED_BYTE_BLOB',
           'PACKAGE_EXECUTION_STATE', '_WIN32_FIND_DATAW',
           'FDAP_BOTTOM', 'DSO_SHUFFLEIMAGES', 'CATINFO_NORMAL',
           'COP_VALUE_ENDSWITH', 'tagLOGPALETTE', 'DesktopWallpaper',
           'COP_LESSTHAN', '_wireSAFEARR_BSTR',
           'HGSC_PICTURESLIBRARY', 'IShellItemArray',
           'COP_VALUE_CONTAINS', 'INamespaceWalk', 'DWPOS_SPAN',
           'KNOWNFOLDER_DEFINITION', 'TBPFLAG',
           '_wireSAFEARR_BRECORD', 'NetworkPlaces', 'IEnumObjects',
           'THBF_NOBACKGROUND', 'IFrameworkInputPane',
           'GPS_VOLATILEPROPERTIES', 'SIATTRIBFLAGS_OR',
           'AVMW_DEFAULT', 'FLVM_ICONS', 'ShellLink',
           '_wireSAFEARR_HAVEIID', 'tagCAPROPVARIANT',
           'IFileOpenDialog', 'CATINFO_EXPANDED', 'wireHICON',
           'DriveTypeCategorizer', '__MIDL_IWinTypes_0008',
           'SHARE_ROLE_MIXED', 'ICustomDestinationList',
           'OpenControlPanel', 'STPF_NONE', 'AVS_FULLSCREEN_PORTRAIT',
           'PDOPS_ERRORS', 'GPS_VOLATILEPROPERTIESONLY',
           'THBF_HIDDEN', 'SIGDN_PARENTRELATIVE', 'tagCAH',
           'DWPOS_TILE', 'PDOPS_CANCELLED', '__MIDL_IAdviseSink_0002',
           'HGSC_VIDEOSLIBRARY', 'IQueryContinue', 'UserNotification',
           'ASSOCIATIONLEVEL', 'ADJACENT_DISPLAY_EDGES',
           'IKnownFolder', 'EDGE_GESTURE_KIND', 'ADE_RIGHT',
           'SHARE_ROLE_CONTRIBUTOR', 'ApplicationDestinations',
           'EGK_KEYBOARD', 'DWPOS_STRETCH', 'AVMW_500',
           'IContextMenuCB', '_STGMEDIUM_UNION',
           'STPF_USEAPPTHUMBNAILWHENACTIVE', '__MIDL_IWinTypes_0003',
           'THB_TOOLTIP', 'IDropTarget',
           'IApplicationActivationManager', 'IEnumShellItems',
           'PES_TERMINATED', 'PES_RUNNING', 'THUMBBUTTON',
           '__MIDL___MIDL_itf_ShObjIdl_core_0003_0088_0001',
           'STPF_USEAPPTHUMBNAILALWAYS', '_RemotableHandle',
           'CATINFO_SHOWEMPTY', 'DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY',
           'KnownFolderManager', 'DEFAULT_FOLDER_MENU_RESTRICTIONS',
           'IPropertyDescriptionList', 'SHARE_ROLE_CUSTOM',
           '_userHGLOBAL', 'tagDVTARGETDEVICE',
           'ApplicationDocumentLists', 'HGSC_MUSICLIBRARY',
           'IEnumFORMATETC', 'KDC_RECENT', 'KF_CATEGORY',
           'AL_MACHINE', 'GPS_EXTRINSICPROPERTIES',
           'LSF_OVERRIDEEXISTING', 'EnumerableObjectCollection',
           'ShellFSFolder', 'IPropertyStore', 'FFFP_EXACTMATCH',
           'APPLICATION_VIEW_STATE', 'tagPALETTEENTRY',
           'DEVICE_SCALE_FACTOR_INVALID', 'tagCACY', 'FDEOR_DEFAULT',
           'DESKTOP_SLIDESHOW_OPTIONS', 'CATINFO_SUBSETTED',
           '_userHMETAFILEPICT', 'wireASYNC_STGMEDIUM', 'STPFLAG',
           'SPACTION_APPLYINGATTRIBS', 'tagCADATE', 'AT_MIMETYPE',
           'wirePSAFEARRAY', 'LOF_PINNEDTONAVPANE',
           'CATINFO_COLLAPSED', 'CT_NOT_CONDITION',
           'SPACTION_DOWNLOADING', 'KF_CATEGORY_PERUSER', 'tagCABSTR',
           'PES_SUSPENDING', 'NDO_PORTRAIT',
           'FDE_SHAREVIOLATION_RESPONSE', 'CATSORT_FLAGS',
           '_userFLAG_STGMEDIUM', 'FLVM_CONTENT', 'APPDOCLISTTYPE',
           'SHARE_ROLE_OWNER', 'CT_OR_CONDITION', 'tagCALPSTR',
           'IPackageExecutionStateChangeNotification']
from comtypes import _check_version; _check_version('')
