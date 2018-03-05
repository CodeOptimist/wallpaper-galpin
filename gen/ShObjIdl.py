# -*- coding: mbcs -*-
# tlb file generated from:
# C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsall.bat x86
# midl C:\Program Files (x86)\Windows Kits\10\Include\10.0.15063.0\um\ShObjIdl.idl
typelib_path = 'C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.15063.0\\um\\ShObjIdl.tlb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
from ctypes.wintypes import tagMSG
WSTRING = c_wchar_p
from comtypes import IUnknown
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import IPersist
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import _FILETIME
from comtypes import BSTR
from comtypes.automation import VARIANT
from comtypes.automation import VARIANT
from ctypes.wintypes import VARIANT_BOOL
from comtypes import wireHWND
from ctypes.wintypes import tagRECT
from ctypes.wintypes import tagPOINT
UINT_PTR = c_ulong
LONG_PTR = c_int
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import tagRECT
from ctypes.wintypes import _POINTL
from ctypes.wintypes import _FILETIME
from comtypes import _COAUTHIDENTITY
from comtypes import tagBIND_OPTS2
from comtypes import tagBIND_OPTS2
from comtypes.persist import IPersistFile
from comtypes import _COSERVERINFO
from comtypes import _COAUTHINFO
from comtypes.automation import IDispatch


class ImageRecompress(CoClass):
    _reg_clsid_ = GUID('{6E33091C-D2F8-4740-B55E-2E11D1477A2C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IImageRecompress(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{505F1513-6B3E-4892-A272-59F8889A4D3E}')
    _idlflags_ = []
ImageRecompress._com_interfaces_ = [IImageRecompress]


# values for enumeration 'NSTCGNI'
NSTCGNI_NEXT = 0
NSTCGNI_NEXTVISIBLE = 1
NSTCGNI_PREV = 2
NSTCGNI_PREVVISIBLE = 3
NSTCGNI_PARENT = 4
NSTCGNI_CHILD = 5
NSTCGNI_FIRSTVISIBLE = 6
NSTCGNI_LASTVISIBLE = 7
NSTCGNI = c_int # enum
class __MIDL_IWinTypes_0001(Union):
    pass
__MIDL_IWinTypes_0001._fields_ = [
    ('dwValue', c_ulong),
    ('pwszName', WSTRING),
]
assert sizeof(__MIDL_IWinTypes_0001) == 4, sizeof(__MIDL_IWinTypes_0001)
assert alignment(__MIDL_IWinTypes_0001) == 4, alignment(__MIDL_IWinTypes_0001)
class IBandSite(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4CF504B0-DE96-11D0-8B3F-00A0C911E8E5}')
    _idlflags_ = []
class IOleWindow(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000114-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IDockingWindow(IOleWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{012DD920-7B26-11D0-8CA9-00A0C92DBFE8}')
    _idlflags_ = []
class IDeskBand(IDockingWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{EB0FE172-1A3A-11D0-89B3-00A0C90A90AC}')
    _idlflags_ = []
class tagBANDSITEINFO(Structure):
    pass
IBandSite._methods_ = [
    COMMETHOD([], HRESULT, 'AddBand',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'EnumBands',
              ( ['in'], c_uint, 'uBand' ),
              ( ['out'], POINTER(c_ulong), 'pdwBandID' )),
    COMMETHOD([], HRESULT, 'RemoteQueryBand',
              ( ['in'], c_ulong, 'dwBandID' ),
              ( ['out'], POINTER(POINTER(IDeskBand)), 'ppstb' ),
              ( ['out'], POINTER(c_ulong), 'pdwState' ),
              ( ['out'], WSTRING, 'pszName' ),
              ( ['in'], c_int, 'cchName' )),
    COMMETHOD([], HRESULT, 'SetBandState',
              ( ['in'], c_ulong, 'dwBandID' ),
              ( ['in'], c_ulong, 'dwMask' ),
              ( ['in'], c_ulong, 'dwState' )),
    COMMETHOD([], HRESULT, 'RemoveBand',
              ( ['in'], c_ulong, 'dwBandID' )),
    COMMETHOD([], HRESULT, 'GetBandObject',
              ( ['in'], c_ulong, 'dwBandID' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
    COMMETHOD([], HRESULT, 'SetBandSiteInfo',
              ( ['in'], POINTER(tagBANDSITEINFO), 'pbsinfo' )),
    COMMETHOD([], HRESULT, 'GetBandSiteInfo',
              ( ['in', 'out'], POINTER(tagBANDSITEINFO), 'pbsinfo' )),
]
################################################################
## code template for IBandSite implementation
##class IBandSite_Impl(object):
##    def AddBand(self, punk):
##        '-no docstring-'
##        #return
##
##    def EnumBands(self, uBand):
##        '-no docstring-'
##        #return pdwBandID
##
##    def RemoteQueryBand(self, dwBandID, cchName):
##        '-no docstring-'
##        #return ppstb, pdwState, pszName
##
##    def SetBandState(self, dwBandID, dwMask, dwState):
##        '-no docstring-'
##        #return
##
##    def RemoveBand(self, dwBandID):
##        '-no docstring-'
##        #return
##
##    def GetBandObject(self, dwBandID, riid):
##        '-no docstring-'
##        #return ppv
##
##    def SetBandSiteInfo(self, pbsinfo):
##        '-no docstring-'
##        #return
##
##    def GetBandSiteInfo(self):
##        '-no docstring-'
##        #return pbsinfo
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
class IShellItem(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{43826D1E-E718-42EE-BC55-A1E261C37BFE}')
    _idlflags_ = []
class IStorage(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000B-0000-0000-C000-000000000046}')
    _idlflags_ = []
class ISequentialStream(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
IImageRecompress._methods_ = [
    COMMETHOD([], HRESULT, 'RecompressImage',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], c_int, 'cx' ),
              ( ['in'], c_int, 'cy' ),
              ( ['in'], c_int, 'iQuality' ),
              ( ['in'], POINTER(IStorage), 'pstg' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstrmOut' )),
]
################################################################
## code template for IImageRecompress implementation
##class IImageRecompress_Impl(object):
##    def RecompressImage(self, psi, cx, cy, iQuality, pstg):
##        '-no docstring-'
##        #return ppstrmOut
##

class _userFLAG_STGMEDIUM(Structure):
    pass
wireFLAG_STGMEDIUM = POINTER(_userFLAG_STGMEDIUM)
class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IMoniker(IPersistStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000F-0000-0000-C000-000000000046}')
    _idlflags_ = []
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

class IBindCtx(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000E-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumMoniker(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000102-0000-0000-C000-000000000046}')
    _idlflags_ = []
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

class IXMLDOMNode(IDispatch):
    _case_insensitive_ = True
    'Core DOM node interface'
    _iid_ = GUID('{2933BF80-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class IXMLDOMDocumentType(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF8B-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']

# values for enumeration 'tagDOMNodeType'
NODE_INVALID = 0
NODE_ELEMENT = 1
NODE_ATTRIBUTE = 2
NODE_TEXT = 3
NODE_CDATA_SECTION = 4
NODE_ENTITY_REFERENCE = 5
NODE_ENTITY = 6
NODE_PROCESSING_INSTRUCTION = 7
NODE_COMMENT = 8
NODE_DOCUMENT = 9
NODE_DOCUMENT_TYPE = 10
NODE_DOCUMENT_FRAGMENT = 11
NODE_NOTATION = 12
tagDOMNodeType = c_int # enum
DOMNodeType = tagDOMNodeType
class IXMLDOMNodeList(IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF82-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class IXMLDOMNamedNodeMap(IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF83-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class IXMLDOMDocument(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF81-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMNode._methods_ = [
    COMMETHOD([dispid(2), helpstring('name of the node'), 'propget'], HRESULT, 'nodeName',
              ( ['out', 'retval'], POINTER(BSTR), 'name' )),
    COMMETHOD([dispid(3), helpstring('value stored in the node'), 'propget'], HRESULT, 'nodeValue',
              ( ['out', 'retval'], POINTER(VARIANT), 'value' )),
    COMMETHOD([dispid(3), helpstring('value stored in the node'), 'propput'], HRESULT, 'nodeValue',
              ( ['in'], VARIANT, 'value' )),
    COMMETHOD([dispid(4), helpstring("the node's type"), 'propget'], HRESULT, 'nodeType',
              ( ['out', 'retval'], POINTER(DOMNodeType), 'type' )),
    COMMETHOD([dispid(6), helpstring('parent of the node'), 'propget'], HRESULT, 'parentNode',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'parent' )),
    COMMETHOD([dispid(7), helpstring("the collection of the node's children"), 'propget'], HRESULT, 'childNodes',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMNodeList))), 'childList' )),
    COMMETHOD([dispid(8), helpstring('first child of the node'), 'propget'], HRESULT, 'firstChild',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'firstChild' )),
    COMMETHOD([dispid(9), helpstring('first child of the node'), 'propget'], HRESULT, 'lastChild',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'lastChild' )),
    COMMETHOD([dispid(10), helpstring('left sibling of the node'), 'propget'], HRESULT, 'previousSibling',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'previousSibling' )),
    COMMETHOD([dispid(11), helpstring('right sibling of the node'), 'propget'], HRESULT, 'nextSibling',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'nextSibling' )),
    COMMETHOD([dispid(12), helpstring("the collection of the node's attributes"), 'propget'], HRESULT, 'attributes',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMNamedNodeMap))), 'attributeMap' )),
    COMMETHOD([dispid(13), helpstring('insert a child node')], HRESULT, 'insertBefore',
              ( ['in'], POINTER(IXMLDOMNode), 'newChild' ),
              ( ['in'], VARIANT, 'refChild' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'outNewChild' )),
    COMMETHOD([dispid(14), helpstring('replace a child node')], HRESULT, 'replaceChild',
              ( ['in'], POINTER(IXMLDOMNode), 'newChild' ),
              ( ['in'], POINTER(IXMLDOMNode), 'oldChild' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'outOldChild' )),
    COMMETHOD([dispid(15), helpstring('remove a child node')], HRESULT, 'removeChild',
              ( ['in'], POINTER(IXMLDOMNode), 'childNode' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'oldChild' )),
    COMMETHOD([dispid(16), helpstring('append a child node')], HRESULT, 'appendChild',
              ( ['in'], POINTER(IXMLDOMNode), 'newChild' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'outNewChild' )),
    COMMETHOD([dispid(17)], HRESULT, 'hasChildNodes',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'hasChild' )),
    COMMETHOD([dispid(18), helpstring('document that contains the node'), 'propget'], HRESULT, 'ownerDocument',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMDocument))), 'DOMDocument' )),
    COMMETHOD([dispid(19)], HRESULT, 'cloneNode',
              ( ['in'], VARIANT_BOOL, 'deep' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'cloneRoot' )),
    COMMETHOD([dispid(21), helpstring('the type of node in string form'), 'propget'], HRESULT, 'nodeTypeString',
              ( ['out', 'retval'], POINTER(BSTR), 'nodeType' )),
    COMMETHOD([dispid(24), helpstring('text content of the node and subtree'), 'propget'], HRESULT, 'text',
              ( ['out', 'retval'], POINTER(BSTR), 'text' )),
    COMMETHOD([dispid(24), helpstring('text content of the node and subtree'), 'propput'], HRESULT, 'text',
              ( ['in'], BSTR, 'text' )),
    COMMETHOD([dispid(22), helpstring('indicates whether node is a default value'), 'propget'], HRESULT, 'specified',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isSpecified' )),
    COMMETHOD([dispid(23), helpstring('pointer to the definition of the node in the DTD or schema'), 'propget'], HRESULT, 'definition',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'definitionNode' )),
    COMMETHOD([dispid(25), helpstring('get the strongly typed value of the node'), 'propget'], HRESULT, 'nodeTypedValue',
              ( ['out', 'retval'], POINTER(VARIANT), 'typedValue' )),
    COMMETHOD([dispid(25), helpstring('get the strongly typed value of the node'), 'propput'], HRESULT, 'nodeTypedValue',
              ( ['in'], VARIANT, 'typedValue' )),
    COMMETHOD([dispid(26), helpstring('the data type of the node'), 'propget'], HRESULT, 'dataType',
              ( ['out', 'retval'], POINTER(VARIANT), 'dataTypeName' )),
    COMMETHOD([dispid(26), helpstring('the data type of the node'), 'propput'], HRESULT, 'dataType',
              ( ['in'], BSTR, 'dataTypeName' )),
    COMMETHOD([dispid(27), helpstring('return the XML source for the node and each of its descendants'), 'propget'], HRESULT, 'xml',
              ( ['out', 'retval'], POINTER(BSTR), 'xmlString' )),
    COMMETHOD([dispid(28), helpstring('apply the stylesheet to the subtree')], HRESULT, 'transformNode',
              ( ['in'], POINTER(IXMLDOMNode), 'stylesheet' ),
              ( ['out', 'retval'], POINTER(BSTR), 'xmlString' )),
    COMMETHOD([dispid(29), helpstring('execute query on the subtree')], HRESULT, 'selectNodes',
              ( ['in'], BSTR, 'queryString' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNodeList)), 'resultList' )),
    COMMETHOD([dispid(30), helpstring('execute query on the subtree')], HRESULT, 'selectSingleNode',
              ( ['in'], BSTR, 'queryString' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'resultNode' )),
    COMMETHOD([dispid(31), helpstring('has sub-tree been completely parsed'), 'propget'], HRESULT, 'parsed',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isParsed' )),
    COMMETHOD([dispid(32), helpstring('the URI for the namespace applying to the node'), 'propget'], HRESULT, 'namespaceURI',
              ( ['out', 'retval'], POINTER(BSTR), 'namespaceURI' )),
    COMMETHOD([dispid(33), helpstring('the prefix for the namespace applying to the node'), 'propget'], HRESULT, 'prefix',
              ( ['out', 'retval'], POINTER(BSTR), 'prefixString' )),
    COMMETHOD([dispid(34), helpstring('the base name of the node (nodename with the prefix stripped off)'), 'propget'], HRESULT, 'baseName',
              ( ['out', 'retval'], POINTER(BSTR), 'nameString' )),
    COMMETHOD([dispid(35), helpstring('apply the stylesheet to the subtree, returning the result through a document or a stream')], HRESULT, 'transformNodeToObject',
              ( ['in'], POINTER(IXMLDOMNode), 'stylesheet' ),
              ( ['in'], VARIANT, 'outputObject' )),
]
################################################################
## code template for IXMLDOMNode implementation
##class IXMLDOMNode_Impl(object):
##    @property
##    def nodeName(self):
##        'name of the node'
##        #return name
##
##    def _get(self):
##        'value stored in the node'
##        #return value
##    def _set(self, value):
##        'value stored in the node'
##    nodeValue = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def nodeType(self):
##        "the node's type"
##        #return type
##
##    @property
##    def parentNode(self):
##        'parent of the node'
##        #return parent
##
##    @property
##    def childNodes(self):
##        "the collection of the node's children"
##        #return childList
##
##    @property
##    def firstChild(self):
##        'first child of the node'
##        #return firstChild
##
##    @property
##    def lastChild(self):
##        'first child of the node'
##        #return lastChild
##
##    @property
##    def previousSibling(self):
##        'left sibling of the node'
##        #return previousSibling
##
##    @property
##    def nextSibling(self):
##        'right sibling of the node'
##        #return nextSibling
##
##    @property
##    def attributes(self):
##        "the collection of the node's attributes"
##        #return attributeMap
##
##    def insertBefore(self, newChild, refChild):
##        'insert a child node'
##        #return outNewChild
##
##    def replaceChild(self, newChild, oldChild):
##        'replace a child node'
##        #return outOldChild
##
##    def removeChild(self, childNode):
##        'remove a child node'
##        #return oldChild
##
##    def appendChild(self, newChild):
##        'append a child node'
##        #return outNewChild
##
##    def hasChildNodes(self):
##        '-no docstring-'
##        #return hasChild
##
##    @property
##    def ownerDocument(self):
##        'document that contains the node'
##        #return DOMDocument
##
##    def cloneNode(self, deep):
##        '-no docstring-'
##        #return cloneRoot
##
##    @property
##    def nodeTypeString(self):
##        'the type of node in string form'
##        #return nodeType
##
##    def _get(self):
##        'text content of the node and subtree'
##        #return text
##    def _set(self, text):
##        'text content of the node and subtree'
##    text = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def specified(self):
##        'indicates whether node is a default value'
##        #return isSpecified
##
##    @property
##    def definition(self):
##        'pointer to the definition of the node in the DTD or schema'
##        #return definitionNode
##
##    def _get(self):
##        'get the strongly typed value of the node'
##        #return typedValue
##    def _set(self, typedValue):
##        'get the strongly typed value of the node'
##    nodeTypedValue = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'the data type of the node'
##        #return dataTypeName
##    def _set(self, dataTypeName):
##        'the data type of the node'
##    dataType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def xml(self):
##        'return the XML source for the node and each of its descendants'
##        #return xmlString
##
##    def transformNode(self, stylesheet):
##        'apply the stylesheet to the subtree'
##        #return xmlString
##
##    def selectNodes(self, queryString):
##        'execute query on the subtree'
##        #return resultList
##
##    def selectSingleNode(self, queryString):
##        'execute query on the subtree'
##        #return resultNode
##
##    @property
##    def parsed(self):
##        'has sub-tree been completely parsed'
##        #return isParsed
##
##    @property
##    def namespaceURI(self):
##        'the URI for the namespace applying to the node'
##        #return namespaceURI
##
##    @property
##    def prefix(self):
##        'the prefix for the namespace applying to the node'
##        #return prefixString
##
##    @property
##    def baseName(self):
##        'the base name of the node (nodename with the prefix stripped off)'
##        #return nameString
##
##    def transformNodeToObject(self, stylesheet, outputObject):
##        'apply the stylesheet to the subtree, returning the result through a document or a stream'
##        #return
##

IXMLDOMDocumentType._methods_ = [
    COMMETHOD([dispid(131), helpstring('name of the document type (root of the tree)'), 'propget'], HRESULT, 'name',
              ( ['out', 'retval'], POINTER(BSTR), 'rootName' )),
    COMMETHOD([dispid(132), helpstring('a list of entities in the document'), 'propget'], HRESULT, 'entities',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNamedNodeMap)), 'entityMap' )),
    COMMETHOD([dispid(133), helpstring('a list of notations in the document'), 'propget'], HRESULT, 'notations',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNamedNodeMap)), 'notationMap' )),
]
################################################################
## code template for IXMLDOMDocumentType implementation
##class IXMLDOMDocumentType_Impl(object):
##    @property
##    def name(self):
##        'name of the document type (root of the tree)'
##        #return rootName
##
##    @property
##    def entities(self):
##        'a list of entities in the document'
##        #return entityMap
##
##    @property
##    def notations(self):
##        'a list of notations in the document'
##        #return notationMap
##


# values for enumeration 'EXPLORER_BROWSER_FILL_FLAGS'
EBF_NONE = 0
EBF_SELECTFROMDATAOBJECT = 256
EBF_NODROPTARGET = 512
EXPLORER_BROWSER_FILL_FLAGS = c_int # enum
IOleWindow._methods_ = [
    COMMETHOD([], HRESULT, 'GetWindow',
              ( ['out'], POINTER(wireHWND), 'phwnd' )),
    COMMETHOD([], HRESULT, 'ContextSensitiveHelp',
              ( ['in'], c_int, 'fEnterMode' )),
]
################################################################
## code template for IOleWindow implementation
##class IOleWindow_Impl(object):
##    def GetWindow(self):
##        '-no docstring-'
##        #return phwnd
##
##    def ContextSensitiveHelp(self, fEnterMode):
##        '-no docstring-'
##        #return
##

IDockingWindow._methods_ = [
    COMMETHOD([], HRESULT, 'ShowDW',
              ( ['in'], c_int, 'fShow' )),
    COMMETHOD([], HRESULT, 'CloseDW',
              ( ['in'], c_ulong, 'dwReserved' )),
    COMMETHOD([], HRESULT, 'ResizeBorderDW',
              ( ['in'], POINTER(tagRECT), 'prcBorder' ),
              ( ['in'], POINTER(IUnknown), 'punkToolbarSite' ),
              ( ['in'], c_int, 'fReserved' )),
]
################################################################
## code template for IDockingWindow implementation
##class IDockingWindow_Impl(object):
##    def ShowDW(self, fShow):
##        '-no docstring-'
##        #return
##
##    def CloseDW(self, dwReserved):
##        '-no docstring-'
##        #return
##
##    def ResizeBorderDW(self, prcBorder, punkToolbarSite, fReserved):
##        '-no docstring-'
##        #return
##

class DESKBANDINFO(Structure):
    pass
IDeskBand._methods_ = [
    COMMETHOD([], HRESULT, 'GetBandInfo',
              ( ['in'], c_ulong, 'dwBandID' ),
              ( ['in'], c_ulong, 'dwViewMode' ),
              ( ['in', 'out'], POINTER(DESKBANDINFO), 'pdbi' )),
]
################################################################
## code template for IDeskBand implementation
##class IDeskBand_Impl(object):
##    def GetBandInfo(self, dwBandID, dwViewMode):
##        '-no docstring-'
##        #return pdbi
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
class _userHPALETTE(Structure):
    pass
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
class TrayBandSiteService(CoClass):
    _reg_clsid_ = GUID('{F60AD0A0-E5E1-45CB-B51A-E15B9F8B2934}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
TrayBandSiteService._com_interfaces_ = [IBandSite]

class IShellItemArray(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B63EA76D-1F85-456F-A19C-48159EFA858B}')
    _idlflags_ = []

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
class _tagpropertykey(Structure):
    pass

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

class IENamespaceTreeControl(CoClass):
    _reg_clsid_ = GUID('{ACE52D03-E5CD-4B20-82FF-E71B11BEAE1D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
IENamespaceTreeControl._com_interfaces_ = [IUnknown]

class IApplicationAssociationRegistrationUI(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1F76A169-F994-40AC-8FC8-0959E8874710}')
    _idlflags_ = []
IApplicationAssociationRegistrationUI._methods_ = [
    COMMETHOD([], HRESULT, 'LaunchAdvancedAssociationUI',
              ( ['in'], WSTRING, 'pszAppRegistryName' )),
]
################################################################
## code template for IApplicationAssociationRegistrationUI implementation
##class IApplicationAssociationRegistrationUI_Impl(object):
##    def LaunchAdvancedAssociationUI(self, pszAppRegistryName):
##        '-no docstring-'
##        #return
##

class FolderViewHost(CoClass):
    _reg_clsid_ = GUID('{20B1CB23-6968-4EB9-B7D4-A66D00D07CEE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IFolderViewHost(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1EA58F02-D55A-411D-B09E-9E65AC21605B}')
    _idlflags_ = []
FolderViewHost._com_interfaces_ = [IFolderViewHost]

class IXMLDOMImplementation(IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF8F-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMImplementation._methods_ = [
    COMMETHOD([dispid(145)], HRESULT, 'hasFeature',
              ( ['in'], BSTR, 'feature' ),
              ( ['in'], BSTR, 'version' ),
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'hasFeature' )),
]
################################################################
## code template for IXMLDOMImplementation implementation
##class IXMLDOMImplementation_Impl(object):
##    def hasFeature(self, feature, version):
##        '-no docstring-'
##        #return hasFeature
##

class IShellBrowser(IOleWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{000214E2-0000-0000-C000-000000000046}')
    _idlflags_ = []
class _RemotableHandle(Structure):
    pass
wireHMENU = POINTER(_RemotableHandle)
class tagOleMenuGroupWidths(Structure):
    pass
class _userHGLOBAL(Structure):
    pass
wireHGLOBAL = POINTER(_userHGLOBAL)
class _BYTE_BLOB(Structure):
    pass
wirePIDL = POINTER(_BYTE_BLOB)
class IShellView(IOleWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{000214E3-0000-0000-C000-000000000046}')
    _idlflags_ = []
IShellBrowser._methods_ = [
    COMMETHOD([], HRESULT, 'InsertMenusSB',
              ( ['in'], wireHMENU, 'hmenuShared' ),
              ( ['in', 'out'], POINTER(tagOleMenuGroupWidths), 'lpMenuWidths' )),
    COMMETHOD([], HRESULT, 'SetMenuSB',
              ( ['in'], wireHMENU, 'hmenuShared' ),
              ( ['in'], wireHGLOBAL, 'holemenuRes' ),
              ( ['in'], wireHWND, 'hwndActiveObject' )),
    COMMETHOD([], HRESULT, 'RemoveMenusSB',
              ( ['in'], wireHMENU, 'hmenuShared' )),
    COMMETHOD([], HRESULT, 'SetStatusTextSB',
              ( ['in'], WSTRING, 'pszStatusText' )),
    COMMETHOD([], HRESULT, 'EnableModelessSB',
              ( ['in'], c_int, 'fEnable' )),
    COMMETHOD([], HRESULT, 'TranslateAcceleratorSB',
              ( ['in'], POINTER(tagMSG), 'pmsg' ),
              ( ['in'], c_ushort, 'wID' )),
    COMMETHOD([], HRESULT, 'BrowseObject',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], c_uint, 'wFlags' )),
    COMMETHOD([], HRESULT, 'GetViewStateStream',
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppStrm' )),
    COMMETHOD([], HRESULT, 'GetControlWindow',
              ( ['in'], c_uint, 'id' ),
              ( ['out'], POINTER(wireHWND), 'phwnd' )),
    COMMETHOD([], HRESULT, 'SendControlMsg',
              ( ['in'], c_uint, 'id' ),
              ( ['in'], c_uint, 'uMsg' ),
              ( ['in'], UINT_PTR, 'wParam' ),
              ( ['in'], LONG_PTR, 'lParam' ),
              ( ['out'], POINTER(LONG_PTR), 'pret' )),
    COMMETHOD([], HRESULT, 'QueryActiveShellView',
              ( ['out'], POINTER(POINTER(IShellView)), 'ppshv' )),
    COMMETHOD([], HRESULT, 'OnViewWindowActive',
              ( ['in'], POINTER(IShellView), 'pshv' )),
    COMMETHOD([], HRESULT, 'SetToolbarItems',
              ( ['in'], LONG_PTR, 'lpButtons' ),
              ( ['in'], c_uint, 'nButtons' ),
              ( ['in'], c_uint, 'uFlags' )),
]
################################################################
## code template for IShellBrowser implementation
##class IShellBrowser_Impl(object):
##    def InsertMenusSB(self, hmenuShared):
##        '-no docstring-'
##        #return lpMenuWidths
##
##    def SetMenuSB(self, hmenuShared, holemenuRes, hwndActiveObject):
##        '-no docstring-'
##        #return
##
##    def RemoveMenusSB(self, hmenuShared):
##        '-no docstring-'
##        #return
##
##    def SetStatusTextSB(self, pszStatusText):
##        '-no docstring-'
##        #return
##
##    def EnableModelessSB(self, fEnable):
##        '-no docstring-'
##        #return
##
##    def TranslateAcceleratorSB(self, pmsg, wID):
##        '-no docstring-'
##        #return
##
##    def BrowseObject(self, pidl, wFlags):
##        '-no docstring-'
##        #return
##
##    def GetViewStateStream(self, grfMode):
##        '-no docstring-'
##        #return ppStrm
##
##    def GetControlWindow(self, id):
##        '-no docstring-'
##        #return phwnd
##
##    def SendControlMsg(self, id, uMsg, wParam, lParam):
##        '-no docstring-'
##        #return pret
##
##    def QueryActiveShellView(self):
##        '-no docstring-'
##        #return ppshv
##
##    def OnViewWindowActive(self, pshv):
##        '-no docstring-'
##        #return
##
##    def SetToolbarItems(self, lpButtons, nButtons, uFlags):
##        '-no docstring-'
##        #return
##


# values for enumeration 'NSTCSTYLE2'
NSTCS2_DEFAULT = 0
NSTCS2_INTERRUPTNOTIFICATIONS = 1
NSTCS2_SHOWNULLSPACEMENU = 2
NSTCS2_DISPLAYPADDING = 4
NSTCS2_DISPLAYPINNEDONLY = 8
NTSCS2_NOSINGLETONAUTOEXPAND = 16
NTSCS2_NEVERINSERTNONENUMERATED = 32
NSTCSTYLE2 = c_int # enum
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

class tagSTATSTG(Structure):
    pass
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

class IExplorerBrowser(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DFD3B6B5-C10C-4BE9-85F6-A66969F402F6}')
    _idlflags_ = []
class FOLDERSETTINGS(Structure):
    pass
class IExplorerBrowserEvents(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{361BBDC7-E6EE-4E13-BE58-58E2240C810F}')
    _idlflags_ = []

# values for enumeration 'EXPLORER_BROWSER_OPTIONS'
EBO_NONE = 0
EBO_NAVIGATEONCE = 1
EBO_SHOWFRAMES = 2
EBO_ALWAYSNAVIGATE = 4
EBO_NOTRAVELLOG = 8
EBO_NOWRAPPERWINDOW = 16
EBO_HTMLSHAREPOINTVIEW = 32
EBO_NOBORDER = 64
EBO_NOPERSISTVIEWSTATE = 128
EXPLORER_BROWSER_OPTIONS = c_int # enum
IExplorerBrowser._methods_ = [
    COMMETHOD([], HRESULT, 'Initialize',
              ( ['in'], wireHWND, 'hwndParent' ),
              ( ['in'], POINTER(tagRECT), 'prc' ),
              ( ['in'], POINTER(FOLDERSETTINGS), 'pfs' )),
    COMMETHOD([], HRESULT, 'Destroy'),
    COMMETHOD([], HRESULT, 'SetRect',
              ( ['in', 'out'], POINTER(c_void_p), 'phdwp' ),
              ( ['in'], tagRECT, 'rcBrowser' )),
    COMMETHOD([], HRESULT, 'SetPropertyBag',
              ( ['in'], WSTRING, 'pszPropertyBag' )),
    COMMETHOD([], HRESULT, 'SetEmptyText',
              ( ['in'], WSTRING, 'pszEmptyText' )),
    COMMETHOD([], HRESULT, 'SetFolderSettings',
              ( ['in'], POINTER(FOLDERSETTINGS), 'pfs' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IExplorerBrowserEvents), 'psbe' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'SetOptions',
              ( ['in'], EXPLORER_BROWSER_OPTIONS, 'dwFlag' )),
    COMMETHOD([], HRESULT, 'GetOptions',
              ( ['out'], POINTER(EXPLORER_BROWSER_OPTIONS), 'pdwFlag' )),
    COMMETHOD([], HRESULT, 'BrowseToIDList',
              ( ['in'], wirePIDL, 'pidl' ),
              ( ['in'], c_uint, 'uFlags' )),
    COMMETHOD([], HRESULT, 'BrowseToObject',
              ( ['in'], POINTER(IUnknown), 'punk' ),
              ( ['in'], c_uint, 'uFlags' )),
    COMMETHOD([], HRESULT, 'FillFromObject',
              ( ['in'], POINTER(IUnknown), 'punk' ),
              ( ['in'], EXPLORER_BROWSER_FILL_FLAGS, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'RemoveAll'),
    COMMETHOD([], HRESULT, 'GetCurrentView',
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
]
################################################################
## code template for IExplorerBrowser implementation
##class IExplorerBrowser_Impl(object):
##    def Initialize(self, hwndParent, prc, pfs):
##        '-no docstring-'
##        #return
##
##    def Destroy(self):
##        '-no docstring-'
##        #return
##
##    def SetRect(self, rcBrowser):
##        '-no docstring-'
##        #return phdwp
##
##    def SetPropertyBag(self, pszPropertyBag):
##        '-no docstring-'
##        #return
##
##    def SetEmptyText(self, pszEmptyText):
##        '-no docstring-'
##        #return
##
##    def SetFolderSettings(self, pfs):
##        '-no docstring-'
##        #return
##
##    def Advise(self, psbe):
##        '-no docstring-'
##        #return pdwCookie
##
##    def Unadvise(self, dwCookie):
##        '-no docstring-'
##        #return
##
##    def SetOptions(self, dwFlag):
##        '-no docstring-'
##        #return
##
##    def GetOptions(self):
##        '-no docstring-'
##        #return pdwFlag
##
##    def BrowseToIDList(self, pidl, uFlags):
##        '-no docstring-'
##        #return
##
##    def BrowseToObject(self, punk, uFlags):
##        '-no docstring-'
##        #return
##
##    def FillFromObject(self, punk, dwFlags):
##        '-no docstring-'
##        #return
##
##    def RemoveAll(self):
##        '-no docstring-'
##        #return
##
##    def GetCurrentView(self, riid):
##        '-no docstring-'
##        #return ppv
##

class AccessibilityDockingService(CoClass):
    _reg_clsid_ = GUID('{29CE1D46-B481-4AA0-A08A-D3EBC8ACA402}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IAccessibilityDockingService(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8849DC22-CEDF-4C95-998D-051419DD3F76}')
    _idlflags_ = []
AccessibilityDockingService._com_interfaces_ = [IAccessibilityDockingService]

IXMLDOMNamedNodeMap._methods_ = [
    COMMETHOD([dispid(83), helpstring('lookup item by name')], HRESULT, 'getNamedItem',
              ( ['in'], BSTR, 'name' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'namedItem' )),
    COMMETHOD([dispid(84), helpstring('set item by name')], HRESULT, 'setNamedItem',
              ( ['in'], POINTER(IXMLDOMNode), 'newItem' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'nameItem' )),
    COMMETHOD([dispid(85), helpstring('remove item by name')], HRESULT, 'removeNamedItem',
              ( ['in'], BSTR, 'name' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'namedItem' )),
    COMMETHOD([dispid(0), helpstring('collection of nodes'), 'propget'], HRESULT, 'item',
              ( ['in'], c_int, 'index' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'listItem' )),
    COMMETHOD([dispid(74), helpstring('number of nodes in the collection'), 'propget'], HRESULT, 'length',
              ( ['out', 'retval'], POINTER(c_int), 'listLength' )),
    COMMETHOD([dispid(87), helpstring('lookup the item by name and namespace')], HRESULT, 'getQualifiedItem',
              ( ['in'], BSTR, 'baseName' ),
              ( ['in'], BSTR, 'namespaceURI' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'qualifiedItem' )),
    COMMETHOD([dispid(88), helpstring('remove the item by name and namespace')], HRESULT, 'removeQualifiedItem',
              ( ['in'], BSTR, 'baseName' ),
              ( ['in'], BSTR, 'namespaceURI' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'qualifiedItem' )),
    COMMETHOD([dispid(89), helpstring('get next node from iterator')], HRESULT, 'nextNode',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'nextItem' )),
    COMMETHOD([dispid(90), helpstring('reset the position of iterator')], HRESULT, 'Reset'),
    COMMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], HRESULT, '_newEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppunk' )),
]
################################################################
## code template for IXMLDOMNamedNodeMap implementation
##class IXMLDOMNamedNodeMap_Impl(object):
##    def getNamedItem(self, name):
##        'lookup item by name'
##        #return namedItem
##
##    def setNamedItem(self, newItem):
##        'set item by name'
##        #return nameItem
##
##    def removeNamedItem(self, name):
##        'remove item by name'
##        #return namedItem
##
##    @property
##    def item(self, index):
##        'collection of nodes'
##        #return listItem
##
##    @property
##    def length(self):
##        'number of nodes in the collection'
##        #return listLength
##
##    def getQualifiedItem(self, baseName, namespaceURI):
##        'lookup the item by name and namespace'
##        #return qualifiedItem
##
##    def removeQualifiedItem(self, baseName, namespaceURI):
##        'remove the item by name and namespace'
##        #return qualifiedItem
##
##    def nextNode(self):
##        'get next node from iterator'
##        #return nextItem
##
##    def Reset(self):
##        'reset the position of iterator'
##        #return
##
##    @property
##    def _newEnum(self):
##        '-no docstring-'
##        #return ppunk
##

class IDataObject(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000010E-0000-0000-C000-000000000046}')
    _idlflags_ = []
IFolderViewHost._methods_ = [
    COMMETHOD([], HRESULT, 'Initialize',
              ( ['in'], wireHWND, 'hwndParent' ),
              ( ['in'], POINTER(IDataObject), 'pdo' ),
              ( ['in'], POINTER(tagRECT), 'prc' )),
]
################################################################
## code template for IFolderViewHost implementation
##class IFolderViewHost_Impl(object):
##    def Initialize(self, hwndParent, pdo, prc):
##        '-no docstring-'
##        #return
##

class tagRemSNB(Structure):
    pass
wireSNB = POINTER(tagRemSNB)
class IEnumSTATSTG(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000D-0000-0000-C000-000000000046}')
    _idlflags_ = []
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

class IXMLDOMElement(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF86-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class IXMLDOMAttribute(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF85-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMElement._methods_ = [
    COMMETHOD([dispid(97), helpstring('get the tagName of the element'), 'propget'], HRESULT, 'tagName',
              ( ['out', 'retval'], POINTER(BSTR), 'tagName' )),
    COMMETHOD([dispid(99), helpstring('look up the string value of an attribute by name')], HRESULT, 'getAttribute',
              ( ['in'], BSTR, 'name' ),
              ( ['out', 'retval'], POINTER(VARIANT), 'value' )),
    COMMETHOD([dispid(100), helpstring('set the string value of an attribute by name')], HRESULT, 'setAttribute',
              ( ['in'], BSTR, 'name' ),
              ( ['in'], VARIANT, 'value' )),
    COMMETHOD([dispid(101), helpstring('remove an attribute by name')], HRESULT, 'removeAttribute',
              ( ['in'], BSTR, 'name' )),
    COMMETHOD([dispid(102), helpstring('look up the attribute node by name')], HRESULT, 'getAttributeNode',
              ( ['in'], BSTR, 'name' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMAttribute)), 'attributeNode' )),
    COMMETHOD([dispid(103), helpstring('set the specified attribute on the element')], HRESULT, 'setAttributeNode',
              ( ['in'], POINTER(IXMLDOMAttribute), 'DOMAttribute' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMAttribute)), 'attributeNode' )),
    COMMETHOD([dispid(104), helpstring('remove the specified attribute')], HRESULT, 'removeAttributeNode',
              ( ['in'], POINTER(IXMLDOMAttribute), 'DOMAttribute' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMAttribute)), 'attributeNode' )),
    COMMETHOD([dispid(105), helpstring('build a list of elements by name')], HRESULT, 'getElementsByTagName',
              ( ['in'], BSTR, 'tagName' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNodeList)), 'resultList' )),
    COMMETHOD([dispid(106), helpstring('collapse all adjacent text nodes in sub-tree')], HRESULT, 'normalize'),
]
################################################################
## code template for IXMLDOMElement implementation
##class IXMLDOMElement_Impl(object):
##    @property
##    def tagName(self):
##        'get the tagName of the element'
##        #return tagName
##
##    def getAttribute(self, name):
##        'look up the string value of an attribute by name'
##        #return value
##
##    def setAttribute(self, name, value):
##        'set the string value of an attribute by name'
##        #return
##
##    def removeAttribute(self, name):
##        'remove an attribute by name'
##        #return
##
##    def getAttributeNode(self, name):
##        'look up the attribute node by name'
##        #return attributeNode
##
##    def setAttributeNode(self, DOMAttribute):
##        'set the specified attribute on the element'
##        #return attributeNode
##
##    def removeAttributeNode(self, DOMAttribute):
##        'remove the specified attribute'
##        #return attributeNode
##
##    def getElementsByTagName(self, tagName):
##        'build a list of elements by name'
##        #return resultList
##
##    def normalize(self):
##        'collapse all adjacent text nodes in sub-tree'
##        #return
##

class ExplorerBrowser(CoClass):
    _reg_clsid_ = GUID('{71F96385-DDD6-48D3-A0C1-AE06E8B055FB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
ExplorerBrowser._com_interfaces_ = [IExplorerBrowser]

class ApplicationAssociationRegistrationUI(CoClass):
    _reg_clsid_ = GUID('{1968106D-F3B5-44CF-890E-116FCB9ECEF1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
ApplicationAssociationRegistrationUI._com_interfaces_ = [IApplicationAssociationRegistrationUI]

class IDesktopGadget(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C1646BC4-F298-4F91-A204-EB2DD1709D1A}')
    _idlflags_ = []
IDesktopGadget._methods_ = [
    COMMETHOD([], HRESULT, 'RunGadget',
              ( ['in'], WSTRING, 'gadgetPath' )),
]
################################################################
## code template for IDesktopGadget implementation
##class IDesktopGadget_Impl(object):
##    def RunGadget(self, gadgetPath):
##        '-no docstring-'
##        #return
##

class DesktopGadget(CoClass):
    _reg_clsid_ = GUID('{924CCC1B-6562-4C85-8657-D177925222B6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
DesktopGadget._com_interfaces_ = [IDesktopGadget]

tagOleMenuGroupWidths._fields_ = [
    ('width', c_int * 6),
]
assert sizeof(tagOleMenuGroupWidths) == 24, sizeof(tagOleMenuGroupWidths)
assert alignment(tagOleMenuGroupWidths) == 4, alignment(tagOleMenuGroupWidths)
class IAttachmentExecute(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{73DB1241-1E85-4581-8E4F-A81E1D0F8C57}')
    _idlflags_ = []

# values for enumeration 'ATTACHMENT_PROMPT'
ATTACHMENT_PROMPT_NONE = 0
ATTACHMENT_PROMPT_SAVE = 1
ATTACHMENT_PROMPT_EXEC = 2
ATTACHMENT_PROMPT_EXEC_OR_SAVE = 3
ATTACHMENT_PROMPT = c_int # enum

# values for enumeration 'ATTACHMENT_ACTION'
ATTACHMENT_ACTION_CANCEL = 0
ATTACHMENT_ACTION_SAVE = 1
ATTACHMENT_ACTION_EXEC = 2
ATTACHMENT_ACTION = c_int # enum
IAttachmentExecute._methods_ = [
    COMMETHOD([], HRESULT, 'SetClientTitle',
              ( ['in'], WSTRING, 'pszTitle' )),
    COMMETHOD([], HRESULT, 'SetClientGuid',
              ( ['in'], POINTER(GUID), 'guid' )),
    COMMETHOD([], HRESULT, 'SetLocalPath',
              ( ['in'], WSTRING, 'pszLocalPath' )),
    COMMETHOD([], HRESULT, 'SetFileName',
              ( ['in'], WSTRING, 'pszFileName' )),
    COMMETHOD([], HRESULT, 'SetSource',
              ( ['in'], WSTRING, 'pszSource' )),
    COMMETHOD([], HRESULT, 'SetReferrer',
              ( ['in'], WSTRING, 'pszReferrer' )),
    COMMETHOD([], HRESULT, 'CheckPolicy'),
    COMMETHOD([], HRESULT, 'Prompt',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], ATTACHMENT_PROMPT, 'Prompt' ),
              ( ['out'], POINTER(ATTACHMENT_ACTION), 'paction' )),
    COMMETHOD([], HRESULT, 'Save'),
    COMMETHOD([], HRESULT, 'Execute',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], WSTRING, 'pszVerb' ),
              ( ['out'], POINTER(c_void_p), 'phProcess' )),
    COMMETHOD([], HRESULT, 'SaveWithUI',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'ClearClientState'),
]
################################################################
## code template for IAttachmentExecute implementation
##class IAttachmentExecute_Impl(object):
##    def SetClientTitle(self, pszTitle):
##        '-no docstring-'
##        #return
##
##    def SetClientGuid(self, guid):
##        '-no docstring-'
##        #return
##
##    def SetLocalPath(self, pszLocalPath):
##        '-no docstring-'
##        #return
##
##    def SetFileName(self, pszFileName):
##        '-no docstring-'
##        #return
##
##    def SetSource(self, pszSource):
##        '-no docstring-'
##        #return
##
##    def SetReferrer(self, pszReferrer):
##        '-no docstring-'
##        #return
##
##    def CheckPolicy(self):
##        '-no docstring-'
##        #return
##
##    def Prompt(self, hwnd, Prompt):
##        '-no docstring-'
##        #return paction
##
##    def Save(self):
##        '-no docstring-'
##        #return
##
##    def Execute(self, hwnd, pszVerb):
##        '-no docstring-'
##        #return phProcess
##
##    def SaveWithUI(self, hwnd):
##        '-no docstring-'
##        #return
##
##    def ClearClientState(self):
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
class IEnumFORMATETC(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000103-0000-0000-C000-000000000046}')
    _idlflags_ = []
class tagFORMATETC(Structure):
    pass
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

DESKBANDINFO._fields_ = [
    ('dwMask', c_ulong),
    ('ptMinSize', _POINTL),
    ('ptMaxSize', _POINTL),
    ('ptIntegral', _POINTL),
    ('ptActual', _POINTL),
    ('wszTitle', c_ushort * 256),
    ('dwModeFlags', c_ulong),
    ('crBkgnd', c_ulong),
]
assert sizeof(DESKBANDINFO) == 556, sizeof(DESKBANDINFO)
assert alignment(DESKBANDINFO) == 4, alignment(DESKBANDINFO)
wireHMONITOR = POINTER(_RemotableHandle)
class IAccessibilityDockingServiceCallback(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{157733FD-A592-42E5-B594-248468C5A81B}')
    _idlflags_ = []
IAccessibilityDockingService._methods_ = [
    COMMETHOD([], HRESULT, 'GetAvailableSize',
              ( ['in'], wireHMONITOR, 'hMonitor' ),
              ( ['out'], POINTER(c_uint), 'pcxFixed' ),
              ( ['out'], POINTER(c_uint), 'pcyMax' )),
    COMMETHOD([], HRESULT, 'DockWindow',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], wireHMONITOR, 'hMonitor' ),
              ( ['in'], c_uint, 'cyRequested' ),
              ( ['in'], POINTER(IAccessibilityDockingServiceCallback), 'pCallback' )),
    COMMETHOD([], HRESULT, 'UndockWindow',
              ( ['in'], wireHWND, 'hwnd' )),
]
################################################################
## code template for IAccessibilityDockingService implementation
##class IAccessibilityDockingService_Impl(object):
##    def GetAvailableSize(self, hMonitor):
##        '-no docstring-'
##        #return pcxFixed, pcyMax
##
##    def DockWindow(self, hwnd, hMonitor, cyRequested, pCallback):
##        '-no docstring-'
##        #return
##
##    def UndockWindow(self, hwnd):
##        '-no docstring-'
##        #return
##

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
class IExecuteCommand(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7F9185B0-CB92-43C5-80A9-92277A4F7B54}')
    _idlflags_ = []
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

tagPALETTEENTRY._fields_ = [
    ('peRed', c_ubyte),
    ('peGreen', c_ubyte),
    ('peBlue', c_ubyte),
    ('peFlags', c_ubyte),
]
assert sizeof(tagPALETTEENTRY) == 4, sizeof(tagPALETTEENTRY)
assert alignment(tagPALETTEENTRY) == 1, alignment(tagPALETTEENTRY)
class _userSTGMEDIUM(Structure):
    pass
class _STGMEDIUM_UNION(Structure):
    pass
class __MIDL_IAdviseSink_0003(Union):
    pass
class _userHMETAFILEPICT(Structure):
    pass
class _userHENHMETAFILE(Structure):
    pass
class _GDI_OBJECT(Structure):
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
_userFLAG_STGMEDIUM._fields_ = [
    ('ContextFlags', c_int),
    ('fPassOwnership', c_int),
    ('Stgmed', _userSTGMEDIUM),
]
assert sizeof(_userFLAG_STGMEDIUM) == 20, sizeof(_userFLAG_STGMEDIUM)
assert alignment(_userFLAG_STGMEDIUM) == 4, alignment(_userFLAG_STGMEDIUM)
IXMLDOMAttribute._methods_ = [
    COMMETHOD([dispid(118), helpstring('get name of the attribute'), 'propget'], HRESULT, 'name',
              ( ['out', 'retval'], POINTER(BSTR), 'attributeName' )),
    COMMETHOD([dispid(120), helpstring('string value of the attribute'), 'propget'], HRESULT, 'value',
              ( ['out', 'retval'], POINTER(VARIANT), 'attributeValue' )),
    COMMETHOD([dispid(120), helpstring('string value of the attribute'), 'propput'], HRESULT, 'value',
              ( ['in'], VARIANT, 'attributeValue' )),
]
################################################################
## code template for IXMLDOMAttribute implementation
##class IXMLDOMAttribute_Impl(object):
##    @property
##    def name(self):
##        'get name of the attribute'
##        #return attributeName
##
##    def _get(self):
##        'string value of the attribute'
##        #return attributeValue
##    def _set(self, attributeValue):
##        'string value of the attribute'
##    value = property(_get, _set, doc = _set.__doc__)
##

class AttachmentServices(CoClass):
    _reg_clsid_ = GUID('{4125DD96-E03A-4103-8F70-E0597D803B9C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
AttachmentServices._com_interfaces_ = [IAttachmentExecute]


# values for enumeration 'UNDOCK_REASON'
UR_RESOLUTION_CHANGE = 0
UR_MONITOR_DISCONNECT = 1
UNDOCK_REASON = c_int # enum
IAccessibilityDockingServiceCallback._methods_ = [
    COMMETHOD([], HRESULT, 'Undocked',
              ( ['in'], UNDOCK_REASON, 'undockReason' )),
]
################################################################
## code template for IAccessibilityDockingServiceCallback implementation
##class IAccessibilityDockingServiceCallback_Impl(object):
##    def Undocked(self, undockReason):
##        '-no docstring-'
##        #return
##

class IVirtualDesktopManager(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A5CD92FF-29BE-454C-8D04-D82879FB3F1B}')
    _idlflags_ = []
IVirtualDesktopManager._methods_ = [
    COMMETHOD([], HRESULT, 'IsWindowOnCurrentVirtualDesktop',
              ( ['in'], wireHWND, 'topLevelWindow' ),
              ( ['out'], POINTER(c_int), 'onCurrentDesktop' )),
    COMMETHOD([], HRESULT, 'GetWindowDesktopId',
              ( ['in'], wireHWND, 'topLevelWindow' ),
              ( ['out'], POINTER(GUID), 'desktopId' )),
    COMMETHOD([], HRESULT, 'MoveWindowToDesktop',
              ( ['in'], wireHWND, 'topLevelWindow' ),
              ( ['in'], POINTER(GUID), 'desktopId' )),
]
################################################################
## code template for IVirtualDesktopManager implementation
##class IVirtualDesktopManager_Impl(object):
##    def IsWindowOnCurrentVirtualDesktop(self, topLevelWindow):
##        '-no docstring-'
##        #return onCurrentDesktop
##
##    def GetWindowDesktopId(self, topLevelWindow):
##        '-no docstring-'
##        #return desktopId
##
##    def MoveWindowToDesktop(self, topLevelWindow, desktopId):
##        '-no docstring-'
##        #return
##

class VirtualDesktopManager(CoClass):
    _reg_clsid_ = GUID('{AA509086-5CA9-4C25-8F95-589D3C07B48A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
VirtualDesktopManager._com_interfaces_ = [IVirtualDesktopManager]

FOLDERSETTINGS._fields_ = [
    ('ViewMode', c_uint),
    ('fFlags', c_uint),
]
assert sizeof(FOLDERSETTINGS) == 8, sizeof(FOLDERSETTINGS)
assert alignment(FOLDERSETTINGS) == 4, alignment(FOLDERSETTINGS)
tagRemSNB._fields_ = [
    ('ulCntStr', c_ulong),
    ('ulCntChar', c_ulong),
    ('rgString', POINTER(c_ushort)),
]
assert sizeof(tagRemSNB) == 12, sizeof(tagRemSNB)
assert alignment(tagRemSNB) == 4, alignment(tagRemSNB)
class ExecuteFolder(CoClass):
    _reg_clsid_ = GUID('{11DBB47C-A525-400B-9E80-A54615A090C0}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
ExecuteFolder._com_interfaces_ = [IExecuteCommand]

class TrayDeskBand(CoClass):
    _reg_clsid_ = GUID('{E6442437-6C68-4F52-94DD-2CFED267EFB9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class ITrayDeskBand(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6D67E846-5B9C-4DB8-9CBC-DDE12F4254F1}')
    _idlflags_ = []
TrayDeskBand._com_interfaces_ = [ITrayDeskBand]

tagBANDSITEINFO._fields_ = [
    ('dwMask', c_ulong),
    ('dwState', c_ulong),
    ('dwStyle', c_ulong),
]
assert sizeof(tagBANDSITEINFO) == 12, sizeof(tagBANDSITEINFO)
assert alignment(tagBANDSITEINFO) == 4, alignment(tagBANDSITEINFO)
ITrayDeskBand._methods_ = [
    COMMETHOD([], HRESULT, 'ShowDeskBand',
              ( ['in'], POINTER(GUID), 'clsid' )),
    COMMETHOD([], HRESULT, 'HideDeskBand',
              ( ['in'], POINTER(GUID), 'clsid' )),
    COMMETHOD([], HRESULT, 'IsDeskBandShown',
              ( ['in'], POINTER(GUID), 'clsid' )),
    COMMETHOD([], HRESULT, 'DeskBandRegistrationChanged'),
]
################################################################
## code template for ITrayDeskBand implementation
##class ITrayDeskBand_Impl(object):
##    def ShowDeskBand(self, clsid):
##        '-no docstring-'
##        #return
##
##    def HideDeskBand(self, clsid):
##        '-no docstring-'
##        #return
##
##    def IsDeskBandShown(self, clsid):
##        '-no docstring-'
##        #return
##
##    def DeskBandRegistrationChanged(self):
##        '-no docstring-'
##        #return
##

_FLAGGED_BYTE_BLOB._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('abData', POINTER(c_ubyte)),
]
assert sizeof(_FLAGGED_BYTE_BLOB) == 12, sizeof(_FLAGGED_BYTE_BLOB)
assert alignment(_FLAGGED_BYTE_BLOB) == 4, alignment(_FLAGGED_BYTE_BLOB)
IExplorerBrowserEvents._methods_ = [
    COMMETHOD([], HRESULT, 'OnNavigationPending',
              ( ['in'], wirePIDL, 'pidlFolder' )),
    COMMETHOD([], HRESULT, 'OnViewCreated',
              ( ['in'], POINTER(IShellView), 'psv' )),
    COMMETHOD([], HRESULT, 'OnNavigationComplete',
              ( ['in'], wirePIDL, 'pidlFolder' )),
    COMMETHOD([], HRESULT, 'OnNavigationFailed',
              ( ['in'], wirePIDL, 'pidlFolder' )),
]
################################################################
## code template for IExplorerBrowserEvents implementation
##class IExplorerBrowserEvents_Impl(object):
##    def OnNavigationPending(self, pidlFolder):
##        '-no docstring-'
##        #return
##
##    def OnViewCreated(self, psv):
##        '-no docstring-'
##        #return
##
##    def OnNavigationComplete(self, pidlFolder):
##        '-no docstring-'
##        #return
##
##    def OnNavigationFailed(self, pidlFolder):
##        '-no docstring-'
##        #return
##

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

class IXMLDOMDocumentFragment(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{3EFAA413-272F-11D2-836F-0000F87A7782}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMDocumentFragment._methods_ = [
]
################################################################
## code template for IXMLDOMDocumentFragment implementation
##class IXMLDOMDocumentFragment_Impl(object):

IShellView._methods_ = [
    COMMETHOD([], HRESULT, 'TranslateAccelerator',
              ( ['in'], POINTER(tagMSG), 'pmsg' )),
    COMMETHOD([], HRESULT, 'EnableModeless',
              ( ['in'], c_int, 'fEnable' )),
    COMMETHOD([], HRESULT, 'UIActivate',
              ( ['in'], c_uint, 'uState' )),
    COMMETHOD([], HRESULT, 'Refresh'),
    COMMETHOD([], HRESULT, 'CreateViewWindow',
              ( ['in'], POINTER(IShellView), 'psvPrevious' ),
              ( ['in'], POINTER(FOLDERSETTINGS), 'pfs' ),
              ( ['in'], POINTER(IShellBrowser), 'psb' ),
              ( ['in'], POINTER(tagRECT), 'prcView' ),
              ( ['out'], POINTER(wireHWND), 'phwnd' )),
    COMMETHOD([], HRESULT, 'DestroyViewWindow'),
    COMMETHOD([], HRESULT, 'GetCurrentInfo',
              ( ['out'], POINTER(FOLDERSETTINGS), 'pfs' )),
    COMMETHOD([], HRESULT, 'AddPropertySheetPages',
              ( ['in'], c_ulong, 'dwReserved' ),
              ( ['in'], LONG_PTR, 'pfn' ),
              ( ['in'], LONG_PTR, 'lParam' )),
    COMMETHOD([], HRESULT, 'SaveViewState'),
    COMMETHOD([], HRESULT, 'SelectItem',
              ( ['in'], wirePIDL, 'pidlItem' ),
              ( ['in'], c_uint, 'uFlags' )),
    COMMETHOD([], HRESULT, 'GetItemObject',
              ( ['in'], c_uint, 'uItem' ),
              ( ['in'], POINTER(GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppv' )),
]
################################################################
## code template for IShellView implementation
##class IShellView_Impl(object):
##    def TranslateAccelerator(self, pmsg):
##        '-no docstring-'
##        #return
##
##    def EnableModeless(self, fEnable):
##        '-no docstring-'
##        #return
##
##    def UIActivate(self, uState):
##        '-no docstring-'
##        #return
##
##    def Refresh(self):
##        '-no docstring-'
##        #return
##
##    def CreateViewWindow(self, psvPrevious, pfs, psb, prcView):
##        '-no docstring-'
##        #return phwnd
##
##    def DestroyViewWindow(self):
##        '-no docstring-'
##        #return
##
##    def GetCurrentInfo(self):
##        '-no docstring-'
##        #return pfs
##
##    def AddPropertySheetPages(self, dwReserved, pfn, lParam):
##        '-no docstring-'
##        #return
##
##    def SaveViewState(self):
##        '-no docstring-'
##        #return
##
##    def SelectItem(self, pidlItem, uFlags):
##        '-no docstring-'
##        #return
##
##    def GetItemObject(self, uItem, riid):
##        '-no docstring-'
##        #return ppv
##

class Library(object):
    name = 'ShellObjects'
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)

class IXMLDOMCharacterData(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF84-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class IXMLDOMText(IXMLDOMCharacterData):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF87-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMCharacterData._methods_ = [
    COMMETHOD([dispid(109), helpstring('value of the node'), 'propget'], HRESULT, 'data',
              ( ['out', 'retval'], POINTER(BSTR), 'data' )),
    COMMETHOD([dispid(109), helpstring('value of the node'), 'propput'], HRESULT, 'data',
              ( ['in'], BSTR, 'data' )),
    COMMETHOD([dispid(110), helpstring('number of characters in value'), 'propget'], HRESULT, 'length',
              ( ['out', 'retval'], POINTER(c_int), 'dataLength' )),
    COMMETHOD([dispid(111), helpstring('retrieve substring of value')], HRESULT, 'substringData',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], c_int, 'count' ),
              ( ['out', 'retval'], POINTER(BSTR), 'data' )),
    COMMETHOD([dispid(112), helpstring('append string to value')], HRESULT, 'appendData',
              ( ['in'], BSTR, 'data' )),
    COMMETHOD([dispid(113), helpstring('insert string into value')], HRESULT, 'insertData',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], BSTR, 'data' )),
    COMMETHOD([dispid(114), helpstring('delete string within the value')], HRESULT, 'deleteData',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], c_int, 'count' )),
    COMMETHOD([dispid(115), helpstring('replace string within the value')], HRESULT, 'replaceData',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], c_int, 'count' ),
              ( ['in'], BSTR, 'data' )),
]
################################################################
## code template for IXMLDOMCharacterData implementation
##class IXMLDOMCharacterData_Impl(object):
##    def _get(self):
##        'value of the node'
##        #return data
##    def _set(self, data):
##        'value of the node'
##    data = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def length(self):
##        'number of characters in value'
##        #return dataLength
##
##    def substringData(self, offset, count):
##        'retrieve substring of value'
##        #return data
##
##    def appendData(self, data):
##        'append string to value'
##        #return
##
##    def insertData(self, offset, data):
##        'insert string into value'
##        #return
##
##    def deleteData(self, offset, count):
##        'delete string within the value'
##        #return
##
##    def replaceData(self, offset, count, data):
##        'replace string within the value'
##        #return
##

IXMLDOMText._methods_ = [
    COMMETHOD([dispid(123), helpstring('split the text node into two text nodes at the position specified')], HRESULT, 'splitText',
              ( ['in'], c_int, 'offset' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMText)), 'rightHandTextNode' )),
]
################################################################
## code template for IXMLDOMText implementation
##class IXMLDOMText_Impl(object):
##    def splitText(self, offset):
##        'split the text node into two text nodes at the position specified'
##        #return rightHandTextNode
##

wireSTGMEDIUM = POINTER(_userSTGMEDIUM)
class IAdviseSink(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000010F-0000-0000-C000-000000000046}')
    _idlflags_ = []
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

class ICDBurn(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3D73A659-E5D0-4D42-AFC0-5121BA425C8D}')
    _idlflags_ = []
ICDBurn._methods_ = [
    COMMETHOD([], HRESULT, 'GetRecorderDriveLetter',
              ( ['out'], WSTRING, 'pszDrive' ),
              ( ['in'], c_uint, 'cch' )),
    COMMETHOD([], HRESULT, 'Burn',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'HasRecordableDrive',
              ( ['out'], POINTER(c_int), 'pfHasRecorder' )),
]
################################################################
## code template for ICDBurn implementation
##class ICDBurn_Impl(object):
##    def GetRecorderDriveLetter(self, cch):
##        '-no docstring-'
##        #return pszDrive
##
##    def Burn(self, hwnd):
##        '-no docstring-'
##        #return
##
##    def HasRecordableDrive(self):
##        '-no docstring-'
##        #return pfHasRecorder
##

class IShellExtInit(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{000214E8-0000-0000-C000-000000000046}')
    _idlflags_ = []
IShellExtInit._methods_ = [
    COMMETHOD([], HRESULT, 'Initialize',
              ( ['in'], wirePIDL, 'pidlFolder' ),
              ( ['in'], POINTER(IDataObject), 'pdtobj' ),
              ( ['in'], c_void_p, 'hkeyProgID' )),
]
################################################################
## code template for IShellExtInit implementation
##class IShellExtInit_Impl(object):
##    def Initialize(self, pidlFolder, pdtobj, hkeyProgID):
##        '-no docstring-'
##        #return
##

class CDBurn(CoClass):
    _reg_clsid_ = GUID('{FBEB8A05-BEEE-4442-804E-409D6C4515E9}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
CDBurn._com_interfaces_ = [ICDBurn]

class IXMLDOMComment(IXMLDOMCharacterData):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF88-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMComment._methods_ = [
]
################################################################
## code template for IXMLDOMComment implementation
##class IXMLDOMComment_Impl(object):

class StartMenuPin(CoClass):
    _reg_clsid_ = GUID('{A2A9545D-A0C2-42B4-9708-A0B2BADD77C8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IStartMenuPinnedList(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4CD19ADA-25A5-4A32-B3B7-347BEE5BE36B}')
    _idlflags_ = []
StartMenuPin._com_interfaces_ = [IStartMenuPinnedList]

IStartMenuPinnedList._methods_ = [
    COMMETHOD([], HRESULT, 'RemoveFromList',
              ( ['in'], POINTER(IShellItem), 'pitem' )),
]
################################################################
## code template for IStartMenuPinnedList implementation
##class IStartMenuPinnedList_Impl(object):
##    def RemoveFromList(self, pitem):
##        '-no docstring-'
##        #return
##

class WebWizardHost(CoClass):
    _reg_clsid_ = GUID('{C827F149-55C1-4D28-935E-57E47CAED973}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IWizardExtension(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C02EA696-86CC-491E-9B23-74394A0444A8}')
    _idlflags_ = []
class IWebWizardExtension(IWizardExtension):
    _case_insensitive_ = True
    _iid_ = GUID('{0E6B3F66-98D1-48C0-A222-FBDE74E2FBC5}')
    _idlflags_ = []
WebWizardHost._com_interfaces_ = [IWebWizardExtension]

class IEnumSTATDATA(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000105-0000-0000-C000-000000000046}')
    _idlflags_ = []
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

class PreviousVersions(CoClass):
    _reg_clsid_ = GUID('{596AB062-B4D2-4215-9F74-E9109B0A8153}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IPreviousVersionsInfo(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{76E54780-AD74-48E3-A695-3BA9A0AFF10D}')
    _idlflags_ = []
PreviousVersions._com_interfaces_ = [IPreviousVersionsInfo]

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

class QueryCancelAutoPlay(CoClass):
    _reg_clsid_ = GUID('{331F1768-05A9-4DDD-B86E-DAE34DDC998A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IQueryCancelAutoPlay(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DDEFE873-6997-4E68-BE26-39B633ADBE12}')
    _idlflags_ = []
QueryCancelAutoPlay._com_interfaces_ = [IQueryCancelAutoPlay]

IQueryCancelAutoPlay._methods_ = [
    COMMETHOD([], HRESULT, 'AllowAutoPlay',
              ( ['in'], WSTRING, 'pszPath' ),
              ( ['in'], c_ulong, 'dwContentType' ),
              ( ['in'], WSTRING, 'pszLabel' ),
              ( ['in'], c_ulong, 'dwSerialNumber' )),
]
################################################################
## code template for IQueryCancelAutoPlay implementation
##class IQueryCancelAutoPlay_Impl(object):
##    def AllowAutoPlay(self, pszPath, dwContentType, pszLabel, dwSerialNumber):
##        '-no docstring-'
##        #return
##

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
IWizardExtension._methods_ = [
    COMMETHOD([], HRESULT, 'AddPages',
              ( ['out'], POINTER(c_void_p), 'aPages' ),
              ( ['in'], c_uint, 'cPages' ),
              ( ['out'], POINTER(c_uint), 'pnPagesAdded' )),
    COMMETHOD([], HRESULT, 'GetFirstPage',
              ( ['out'], POINTER(c_void_p), 'phpage' )),
    COMMETHOD([], HRESULT, 'GetLastPage',
              ( ['out'], POINTER(c_void_p), 'phpage' )),
]
################################################################
## code template for IWizardExtension implementation
##class IWizardExtension_Impl(object):
##    def AddPages(self, cPages):
##        '-no docstring-'
##        #return aPages, pnPagesAdded
##
##    def GetFirstPage(self):
##        '-no docstring-'
##        #return phpage
##
##    def GetLastPage(self):
##        '-no docstring-'
##        #return phpage
##

IWebWizardExtension._methods_ = [
    COMMETHOD([], HRESULT, 'SetInitialURL',
              ( ['in'], WSTRING, 'pszURL' )),
    COMMETHOD([], HRESULT, 'SetErrorURL',
              ( ['in'], WSTRING, 'pszErrorURL' )),
]
################################################################
## code template for IWebWizardExtension implementation
##class IWebWizardExtension_Impl(object):
##    def SetInitialURL(self, pszURL):
##        '-no docstring-'
##        #return
##
##    def SetErrorURL(self, pszErrorURL):
##        '-no docstring-'
##        #return
##

class ICategorizer(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A3B14589-9174-49A8-89A3-06A1AE2B9BA7}')
    _idlflags_ = []
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

class TimeCategorizer(CoClass):
    _reg_clsid_ = GUID('{3BB4118F-DDFD-4D30-A348-9FB5D6BF1AFE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
TimeCategorizer._com_interfaces_ = [ICategorizer]

class IXMLDOMCDATASection(IXMLDOMText):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF8A-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMCDATASection._methods_ = [
]
################################################################
## code template for IXMLDOMCDATASection implementation
##class IXMLDOMCDATASection_Impl(object):

class FSCopyHandler(CoClass):
    _reg_clsid_ = GUID('{D197380A-0A79-4DC8-A033-ED882C2FA14B}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
FSCopyHandler._com_interfaces_ = [IUnknown]


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

class _userCLIPFORMAT(Structure):
    pass
wireCLIPFORMAT = POINTER(_userCLIPFORMAT)
class tagDVTARGETDEVICE(Structure):
    pass
tagFORMATETC._fields_ = [
    ('cfFormat', wireCLIPFORMAT),
    ('ptd', POINTER(tagDVTARGETDEVICE)),
    ('dwAspect', c_ulong),
    ('lindex', c_int),
    ('tymed', c_ulong),
]
assert sizeof(tagFORMATETC) == 20, sizeof(tagFORMATETC)
assert alignment(tagFORMATETC) == 4, alignment(tagFORMATETC)
tagSTATDATA._fields_ = [
    ('formatetc', tagFORMATETC),
    ('advf', c_ulong),
    ('pAdvSink', POINTER(IAdviseSink)),
    ('dwConnection', c_ulong),
]
assert sizeof(tagSTATDATA) == 32, sizeof(tagSTATDATA)
assert alignment(tagSTATDATA) == 4, alignment(tagSTATDATA)
class DocPropShellExtension(CoClass):
    _reg_clsid_ = GUID('{883373C3-BF89-11D1-BE35-080036B11A03}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
DocPropShellExtension._com_interfaces_ = [IShellExtInit]

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
class IPublishingWizard(IWizardExtension):
    _case_insensitive_ = True
    _iid_ = GUID('{AA9198BB-CCEC-472D-BEED-19A4F6733F7A}')
    _idlflags_ = []
IPublishingWizard._methods_ = [
    COMMETHOD([], HRESULT, 'Initialize',
              ( ['in'], POINTER(IDataObject), 'pdo' ),
              ( ['in'], c_ulong, 'dwOptions' ),
              ( ['in'], WSTRING, 'pszServiceScope' )),
    COMMETHOD([], HRESULT, 'GetTransferManifest',
              ( ['out'], POINTER(HRESULT), 'phrFromTransfer' ),
              ( ['out'], POINTER(POINTER(IXMLDOMDocument)), 'pdocManifest' )),
]
################################################################
## code template for IPublishingWizard implementation
##class IPublishingWizard_Impl(object):
##    def Initialize(self, pdo, dwOptions, pszServiceScope):
##        '-no docstring-'
##        #return
##
##    def GetTransferManifest(self):
##        '-no docstring-'
##        #return phrFromTransfer, pdocManifest
##

_tagpropertykey._fields_ = [
    ('fmtid', GUID),
    ('pid', c_ulong),
]
assert sizeof(_tagpropertykey) == 20, sizeof(_tagpropertykey)
assert alignment(_tagpropertykey) == 4, alignment(_tagpropertykey)
class IXMLDOMProcessingInstruction(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF89-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMProcessingInstruction._methods_ = [
    COMMETHOD([dispid(127), helpstring('the target'), 'propget'], HRESULT, 'target',
              ( ['out', 'retval'], POINTER(BSTR), 'name' )),
    COMMETHOD([dispid(128), helpstring('the data'), 'propget'], HRESULT, 'data',
              ( ['out', 'retval'], POINTER(BSTR), 'value' )),
    COMMETHOD([dispid(128), helpstring('the data'), 'propput'], HRESULT, 'data',
              ( ['in'], BSTR, 'value' )),
]
################################################################
## code template for IXMLDOMProcessingInstruction implementation
##class IXMLDOMProcessingInstruction_Impl(object):
##    @property
##    def target(self):
##        'the target'
##        #return name
##
##    def _get(self):
##        'the data'
##        #return value
##    def _set(self, value):
##        'the data'
##    data = property(_get, _set, doc = _set.__doc__)
##

IPreviousVersionsInfo._methods_ = [
    COMMETHOD([], HRESULT, 'AreSnapshotsAvailable',
              ( ['in'], WSTRING, 'pszPath' ),
              ( ['in'], c_int, 'fOkToBeSlow' ),
              ( ['out'], POINTER(c_int), 'pfAvailable' )),
]
################################################################
## code template for IPreviousVersionsInfo implementation
##class IPreviousVersionsInfo_Impl(object):
##    def AreSnapshotsAvailable(self, pszPath, fOkToBeSlow):
##        '-no docstring-'
##        #return pfAvailable
##

class NamespaceTreeControl(CoClass):
    _reg_clsid_ = GUID('{AE054212-3535-4430-83ED-D501AA6680E6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class INameSpaceTreeControl(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{028212A3-B627-47E9-8856-C14265554E4F}')
    _idlflags_ = []
class INameSpaceTreeControl2(INameSpaceTreeControl):
    _case_insensitive_ = True
    _iid_ = GUID('{7CC7AED8-290E-49BC-8945-C1401CC9306C}')
    _idlflags_ = []
NamespaceTreeControl._com_interfaces_ = [INameSpaceTreeControl2]

class IShellItemFilter(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2659B475-EEB8-48B7-8F07-B378810F48CF}')
    _idlflags_ = []
INameSpaceTreeControl._methods_ = [
    COMMETHOD([], HRESULT, 'Initialize',
              ( ['in'], wireHWND, 'hwndParent' ),
              ( ['in'], POINTER(tagRECT), 'prc' ),
              ( ['in'], c_ulong, 'nsctsFlags' )),
    COMMETHOD([], HRESULT, 'TreeAdvise',
              ( ['in'], POINTER(IUnknown), 'punk' ),
              ( ['out'], POINTER(c_ulong), 'pdwCookie' )),
    COMMETHOD([], HRESULT, 'TreeUnadvise',
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'AppendRoot',
              ( ['in'], POINTER(IShellItem), 'psiRoot' ),
              ( ['in'], c_ulong, 'grfEnumFlags' ),
              ( ['in'], c_ulong, 'grfRootStyle' ),
              ( ['in'], POINTER(IShellItemFilter), 'pif' )),
    COMMETHOD([], HRESULT, 'InsertRoot',
              ( ['in'], c_int, 'iIndex' ),
              ( ['in'], POINTER(IShellItem), 'psiRoot' ),
              ( ['in'], c_ulong, 'grfEnumFlags' ),
              ( ['in'], c_ulong, 'grfRootStyle' ),
              ( ['in'], POINTER(IShellItemFilter), 'pif' )),
    COMMETHOD([], HRESULT, 'RemoveRoot',
              ( ['in'], POINTER(IShellItem), 'psiRoot' )),
    COMMETHOD([], HRESULT, 'RemoveAllRoots'),
    COMMETHOD([], HRESULT, 'GetRootItems',
              ( ['out'], POINTER(POINTER(IShellItemArray)), 'ppsiaRootItems' )),
    COMMETHOD([], HRESULT, 'SetItemState',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], c_ulong, 'nstcisMask' ),
              ( ['in'], c_ulong, 'nstcisFlags' )),
    COMMETHOD([], HRESULT, 'GetItemState',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], c_ulong, 'nstcisMask' ),
              ( ['out'], POINTER(c_ulong), 'pnstcisFlags' )),
    COMMETHOD([], HRESULT, 'GetSelectedItems',
              ( ['out'], POINTER(POINTER(IShellItemArray)), 'psiaItems' )),
    COMMETHOD([], HRESULT, 'GetItemCustomState',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['out'], POINTER(c_int), 'piStateNumber' )),
    COMMETHOD([], HRESULT, 'SetItemCustomState',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], c_int, 'iStateNumber' )),
    COMMETHOD([], HRESULT, 'EnsureItemVisible',
              ( ['in'], POINTER(IShellItem), 'psi' )),
    COMMETHOD([], HRESULT, 'SetTheme',
              ( ['in'], WSTRING, 'pszTheme' )),
    COMMETHOD([], HRESULT, 'GetNextItem',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['in'], NSTCGNI, 'nstcgi' ),
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsiNext' )),
    COMMETHOD([], HRESULT, 'HitTest',
              ( ['in'], POINTER(tagPOINT), 'ppt' ),
              ( ['out'], POINTER(POINTER(IShellItem)), 'ppsiOut' )),
    COMMETHOD([], HRESULT, 'GetItemRect',
              ( ['in'], POINTER(IShellItem), 'psi' ),
              ( ['out'], POINTER(tagRECT), 'prect' )),
    COMMETHOD([], HRESULT, 'CollapseAll'),
]
################################################################
## code template for INameSpaceTreeControl implementation
##class INameSpaceTreeControl_Impl(object):
##    def Initialize(self, hwndParent, prc, nsctsFlags):
##        '-no docstring-'
##        #return
##
##    def TreeAdvise(self, punk):
##        '-no docstring-'
##        #return pdwCookie
##
##    def TreeUnadvise(self, dwCookie):
##        '-no docstring-'
##        #return
##
##    def AppendRoot(self, psiRoot, grfEnumFlags, grfRootStyle, pif):
##        '-no docstring-'
##        #return
##
##    def InsertRoot(self, iIndex, psiRoot, grfEnumFlags, grfRootStyle, pif):
##        '-no docstring-'
##        #return
##
##    def RemoveRoot(self, psiRoot):
##        '-no docstring-'
##        #return
##
##    def RemoveAllRoots(self):
##        '-no docstring-'
##        #return
##
##    def GetRootItems(self):
##        '-no docstring-'
##        #return ppsiaRootItems
##
##    def SetItemState(self, psi, nstcisMask, nstcisFlags):
##        '-no docstring-'
##        #return
##
##    def GetItemState(self, psi, nstcisMask):
##        '-no docstring-'
##        #return pnstcisFlags
##
##    def GetSelectedItems(self):
##        '-no docstring-'
##        #return psiaItems
##
##    def GetItemCustomState(self, psi):
##        '-no docstring-'
##        #return piStateNumber
##
##    def SetItemCustomState(self, psi, iStateNumber):
##        '-no docstring-'
##        #return
##
##    def EnsureItemVisible(self, psi):
##        '-no docstring-'
##        #return
##
##    def SetTheme(self, pszTheme):
##        '-no docstring-'
##        #return
##
##    def GetNextItem(self, psi, nstcgi):
##        '-no docstring-'
##        #return ppsiNext
##
##    def HitTest(self, ppt):
##        '-no docstring-'
##        #return ppsiOut
##
##    def GetItemRect(self, psi):
##        '-no docstring-'
##        #return prect
##
##    def CollapseAll(self):
##        '-no docstring-'
##        #return
##

INameSpaceTreeControl2._methods_ = [
    COMMETHOD([], HRESULT, 'SetControlStyle',
              ( ['in'], c_ulong, 'nstcsMask' ),
              ( ['in'], c_ulong, 'nstcsStyle' )),
    COMMETHOD([], HRESULT, 'GetControlStyle',
              ( ['in'], c_ulong, 'nstcsMask' ),
              ( ['out'], POINTER(c_ulong), 'pnstcsStyle' )),
    COMMETHOD([], HRESULT, 'SetControlStyle2',
              ( ['in'], NSTCSTYLE2, 'nstcsMask' ),
              ( ['in'], NSTCSTYLE2, 'nstcsStyle' )),
    COMMETHOD([], HRESULT, 'GetControlStyle2',
              ( ['in'], NSTCSTYLE2, 'nstcsMask' ),
              ( ['out'], POINTER(NSTCSTYLE2), 'pnstcsStyle' )),
]
################################################################
## code template for INameSpaceTreeControl2 implementation
##class INameSpaceTreeControl2_Impl(object):
##    def SetControlStyle(self, nstcsMask, nstcsStyle):
##        '-no docstring-'
##        #return
##
##    def GetControlStyle(self, nstcsMask):
##        '-no docstring-'
##        #return pnstcsStyle
##
##    def SetControlStyle2(self, nstcsMask, nstcsStyle):
##        '-no docstring-'
##        #return
##
##    def GetControlStyle2(self, nstcsMask):
##        '-no docstring-'
##        #return pnstcsStyle
##

class PublishingWizard(CoClass):
    _reg_clsid_ = GUID('{6B33163C-76A5-4B6C-BF21-45DE9CD503A1}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
PublishingWizard._com_interfaces_ = [IPublishingWizard]

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

class ImageProperties(CoClass):
    _reg_clsid_ = GUID('{7AB770C7-0E23-4D7A-8AA2-19BFAD479829}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
ImageProperties._com_interfaces_ = [IPersistFile]

_BYTE_BLOB._fields_ = [
    ('clSize', c_ulong),
    ('abData', POINTER(c_ubyte)),
]
assert sizeof(_BYTE_BLOB) == 8, sizeof(_BYTE_BLOB)
assert alignment(_BYTE_BLOB) == 4, alignment(_BYTE_BLOB)
class IXMLDOMEntityReference(IXMLDOMNode):
    _case_insensitive_ = True
    _iid_ = GUID('{2933BF8E-7B36-11D2-B20E-00C04F983E60}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMEntityReference._methods_ = [
]
################################################################
## code template for IXMLDOMEntityReference implementation
##class IXMLDOMEntityReference_Impl(object):

class InternetPrintOrdering(CoClass):
    _reg_clsid_ = GUID('{ADD36AA8-751A-4579-A266-D66F5202CCBB}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
class IDropTarget(IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000122-0000-0000-C000-000000000046}')
    _idlflags_ = []
InternetPrintOrdering._com_interfaces_ = [IDropTarget]

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

class IXMLDOMParseError(IDispatch):
    _case_insensitive_ = True
    'structure for reporting parser errors'
    _iid_ = GUID('{3EFAA426-272F-11D2-836F-0000F87A7782}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
IXMLDOMDocument._methods_ = [
    COMMETHOD([dispid(38), helpstring('node corresponding to the DOCTYPE'), 'propget'], HRESULT, 'doctype',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMDocumentType))), 'documentType' )),
    COMMETHOD([dispid(39), helpstring('info on this DOM implementation'), 'propget'], HRESULT, 'implementation',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMImplementation))), 'impl' )),
    COMMETHOD([dispid(40), helpstring('the root of the tree'), 'propget'], HRESULT, 'documentElement',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMElement))), 'DOMElement' )),
    COMMETHOD([dispid(40), helpstring('the root of the tree'), 'propputref'], HRESULT, 'documentElement',
              ( ['in'], POINTER(IXMLDOMElement), 'DOMElement' )),
    COMMETHOD([dispid(41), helpstring('create an Element node')], HRESULT, 'createElement',
              ( ['in'], BSTR, 'tagName' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMElement)), 'element' )),
    COMMETHOD([dispid(42), helpstring('create a DocumentFragment node')], HRESULT, 'createDocumentFragment',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMDocumentFragment))), 'docFrag' )),
    COMMETHOD([dispid(43), helpstring('create a text node')], HRESULT, 'createTextNode',
              ( ['in'], BSTR, 'data' ),
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMText))), 'text' )),
    COMMETHOD([dispid(44), helpstring('create a comment node')], HRESULT, 'createComment',
              ( ['in'], BSTR, 'data' ),
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMComment))), 'comment' )),
    COMMETHOD([dispid(45), helpstring('create a CDATA section node')], HRESULT, 'createCDATASection',
              ( ['in'], BSTR, 'data' ),
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMCDATASection))), 'cdata' )),
    COMMETHOD([dispid(46), helpstring('create a processing instruction node')], HRESULT, 'createProcessingInstruction',
              ( ['in'], BSTR, 'target' ),
              ( ['in'], BSTR, 'data' ),
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMProcessingInstruction))), 'pi' )),
    COMMETHOD([dispid(47), helpstring('create an attribute node')], HRESULT, 'createAttribute',
              ( ['in'], BSTR, 'name' ),
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMAttribute))), 'attribute' )),
    COMMETHOD([dispid(49), helpstring('create an entity reference node')], HRESULT, 'createEntityReference',
              ( ['in'], BSTR, 'name' ),
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMEntityReference))), 'entityRef' )),
    COMMETHOD([dispid(50), helpstring('build a list of elements by name')], HRESULT, 'getElementsByTagName',
              ( ['in'], BSTR, 'tagName' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNodeList)), 'resultList' )),
    COMMETHOD([dispid(54), helpstring('create a node of the specified node type and name')], HRESULT, 'createNode',
              ( ['in'], VARIANT, 'type' ),
              ( ['in'], BSTR, 'name' ),
              ( ['in'], BSTR, 'namespaceURI' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'node' )),
    COMMETHOD([dispid(56), helpstring("retrieve node from it's ID")], HRESULT, 'nodeFromID',
              ( ['in'], BSTR, 'idString' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'node' )),
    COMMETHOD([dispid(58), helpstring('load document from the specified XML source')], HRESULT, 'Load',
              ( ['in'], VARIANT, 'xmlSource' ),
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isSuccessful' )),
    COMMETHOD([dispid(-525), helpstring('get the state of the XML document'), 'propget'], HRESULT, 'readyState',
              ( ['out', 'retval'], POINTER(c_int), 'value' )),
    COMMETHOD([dispid(59), helpstring('get the last parser error'), 'propget'], HRESULT, 'parseError',
              ( ['out', 'retval'], POINTER(POINTER(POINTER(IXMLDOMParseError))), 'errorObj' )),
    COMMETHOD([dispid(60), helpstring('get the URL for the loaded XML document'), 'propget'], HRESULT, 'url',
              ( ['out', 'retval'], POINTER(BSTR), 'urlString' )),
    COMMETHOD([dispid(61), helpstring('flag for asynchronous download'), 'propget'], HRESULT, 'async',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isAsync' )),
    COMMETHOD([dispid(61), helpstring('flag for asynchronous download'), 'propput'], HRESULT, 'async',
              ( ['in'], VARIANT_BOOL, 'isAsync' )),
    COMMETHOD([dispid(62), helpstring('abort an asynchronous download')], HRESULT, 'abort'),
    COMMETHOD([dispid(63), helpstring('load the document from a string')], HRESULT, 'loadXML',
              ( ['in'], BSTR, 'bstrXML' ),
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isSuccessful' )),
    COMMETHOD([dispid(64), helpstring('save the document to a specified desination')], HRESULT, 'Save',
              ( ['in'], VARIANT, 'desination' )),
    COMMETHOD([dispid(65), helpstring('indicates whether the parser performs validation'), 'propget'], HRESULT, 'validateOnParse',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isValidating' )),
    COMMETHOD([dispid(65), helpstring('indicates whether the parser performs validation'), 'propput'], HRESULT, 'validateOnParse',
              ( ['in'], VARIANT_BOOL, 'isValidating' )),
    COMMETHOD([dispid(66), helpstring('indicates whether the parser resolves references to external DTD/Entities/Schema'), 'propget'], HRESULT, 'resolveExternals',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isResolving' )),
    COMMETHOD([dispid(66), helpstring('indicates whether the parser resolves references to external DTD/Entities/Schema'), 'propput'], HRESULT, 'resolveExternals',
              ( ['in'], VARIANT_BOOL, 'isResolving' )),
    COMMETHOD([dispid(67), helpstring('indicates whether the parser preserves whitespace'), 'propget'], HRESULT, 'preserveWhiteSpace',
              ( ['out', 'retval'], POINTER(VARIANT_BOOL), 'isPreserving' )),
    COMMETHOD([dispid(67), helpstring('indicates whether the parser preserves whitespace'), 'propput'], HRESULT, 'preserveWhiteSpace',
              ( ['in'], VARIANT_BOOL, 'isPreserving' )),
    COMMETHOD([dispid(68), helpstring('register a readystatechange event handler'), 'propput'], HRESULT, 'onreadystatechange',
              ( ['in'], VARIANT, 'rhs' )),
    COMMETHOD([dispid(69), helpstring('register an ondataavailable event handler'), 'propput'], HRESULT, 'ondataavailable',
              ( ['in'], VARIANT, 'rhs' )),
    COMMETHOD([dispid(70), helpstring('register an ontransformnode event handler'), 'propput'], HRESULT, 'ontransformnode',
              ( ['in'], VARIANT, 'rhs' )),
]
################################################################
## code template for IXMLDOMDocument implementation
##class IXMLDOMDocument_Impl(object):
##    @property
##    def doctype(self):
##        'node corresponding to the DOCTYPE'
##        #return documentType
##
##    @property
##    def implementation(self):
##        'info on this DOM implementation'
##        #return impl
##
##    def documentElement(self, DOMElement):
##        'the root of the tree'
##        #return
##
##    def createElement(self, tagName):
##        'create an Element node'
##        #return element
##
##    def createDocumentFragment(self):
##        'create a DocumentFragment node'
##        #return docFrag
##
##    def createTextNode(self, data):
##        'create a text node'
##        #return text
##
##    def createComment(self, data):
##        'create a comment node'
##        #return comment
##
##    def createCDATASection(self, data):
##        'create a CDATA section node'
##        #return cdata
##
##    def createProcessingInstruction(self, target, data):
##        'create a processing instruction node'
##        #return pi
##
##    def createAttribute(self, name):
##        'create an attribute node'
##        #return attribute
##
##    def createEntityReference(self, name):
##        'create an entity reference node'
##        #return entityRef
##
##    def getElementsByTagName(self, tagName):
##        'build a list of elements by name'
##        #return resultList
##
##    def createNode(self, type, name, namespaceURI):
##        'create a node of the specified node type and name'
##        #return node
##
##    def nodeFromID(self, idString):
##        "retrieve node from it's ID"
##        #return node
##
##    def Load(self, xmlSource):
##        'load document from the specified XML source'
##        #return isSuccessful
##
##    @property
##    def readyState(self):
##        'get the state of the XML document'
##        #return value
##
##    @property
##    def parseError(self):
##        'get the last parser error'
##        #return errorObj
##
##    @property
##    def url(self):
##        'get the URL for the loaded XML document'
##        #return urlString
##
##    def _get(self):
##        'flag for asynchronous download'
##        #return isAsync
##    def _set(self, isAsync):
##        'flag for asynchronous download'
##    async = property(_get, _set, doc = _set.__doc__)
##
##    def abort(self):
##        'abort an asynchronous download'
##        #return
##
##    def loadXML(self, bstrXML):
##        'load the document from a string'
##        #return isSuccessful
##
##    def Save(self, desination):
##        'save the document to a specified desination'
##        #return
##
##    def _get(self):
##        'indicates whether the parser performs validation'
##        #return isValidating
##    def _set(self, isValidating):
##        'indicates whether the parser performs validation'
##    validateOnParse = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'indicates whether the parser resolves references to external DTD/Entities/Schema'
##        #return isResolving
##    def _set(self, isResolving):
##        'indicates whether the parser resolves references to external DTD/Entities/Schema'
##    resolveExternals = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        'indicates whether the parser preserves whitespace'
##        #return isPreserving
##    def _set(self, isPreserving):
##        'indicates whether the parser preserves whitespace'
##    preserveWhiteSpace = property(_get, _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        'register a readystatechange event handler'
##    onreadystatechange = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        'register an ondataavailable event handler'
##    ondataavailable = property(fset = _set, doc = _set.__doc__)
##
##    def _set(self, rhs):
##        'register an ontransformnode event handler'
##    ontransformnode = property(fset = _set, doc = _set.__doc__)
##

IXMLDOMParseError._methods_ = [
    COMMETHOD([dispid(0), helpstring('the error code'), 'propget'], HRESULT, 'errorCode',
              ( ['out', 'retval'], POINTER(c_int), 'errorCode' )),
    COMMETHOD([dispid(179), helpstring('the URL of the XML document containing the error'), 'propget'], HRESULT, 'url',
              ( ['out', 'retval'], POINTER(BSTR), 'urlString' )),
    COMMETHOD([dispid(180), helpstring('the cause of the error'), 'propget'], HRESULT, 'reason',
              ( ['out', 'retval'], POINTER(BSTR), 'reasonString' )),
    COMMETHOD([dispid(181), helpstring('the data where the error occurred'), 'propget'], HRESULT, 'srcText',
              ( ['out', 'retval'], POINTER(BSTR), 'sourceString' )),
    COMMETHOD([dispid(182), helpstring('the line number in the XML document where the error occurred'), 'propget'], HRESULT, 'line',
              ( ['out', 'retval'], POINTER(c_int), 'lineNumber' )),
    COMMETHOD([dispid(183), helpstring('the character position in the line containing the error'), 'propget'], HRESULT, 'linepos',
              ( ['out', 'retval'], POINTER(c_int), 'linePosition' )),
    COMMETHOD([dispid(184), helpstring('the absolute file position in the XML document containing the error'), 'propget'], HRESULT, 'filepos',
              ( ['out', 'retval'], POINTER(c_int), 'filePosition' )),
]
################################################################
## code template for IXMLDOMParseError implementation
##class IXMLDOMParseError_Impl(object):
##    @property
##    def errorCode(self):
##        'the error code'
##        #return errorCode
##
##    @property
##    def url(self):
##        'the URL of the XML document containing the error'
##        #return urlString
##
##    @property
##    def reason(self):
##        'the cause of the error'
##        #return reasonString
##
##    @property
##    def srcText(self):
##        'the data where the error occurred'
##        #return sourceString
##
##    @property
##    def line(self):
##        'the line number in the XML document where the error occurred'
##        #return lineNumber
##
##    @property
##    def linepos(self):
##        'the character position in the line containing the error'
##        #return linePosition
##
##    @property
##    def filepos(self):
##        'the absolute file position in the XML document containing the error'
##        #return filePosition
##

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
class AlphabeticalCategorizer(CoClass):
    _reg_clsid_ = GUID('{3C2654C6-7372-4F6B-B310-55D6128F49D2}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
AlphabeticalCategorizer._com_interfaces_ = [ICategorizer]

class PublishDropTarget(CoClass):
    _reg_clsid_ = GUID('{CC6EEFFB-43F6-46C5-9619-51D571967F7D}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
PublishDropTarget._com_interfaces_ = [IDropTarget]


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

class MergedCategorizer(CoClass):
    _reg_clsid_ = GUID('{8E827C11-33E7-4BC1-B242-8CD9A1C2B304}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{50A7E9B1-70EF-11D1-B75A-00A0C90564FE}', 1, 0)
MergedCategorizer._com_interfaces_ = [ICategorizer]

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

IXMLDOMNodeList._methods_ = [
    COMMETHOD([dispid(0), helpstring('collection of nodes'), 'propget'], HRESULT, 'item',
              ( ['in'], c_int, 'index' ),
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'listItem' )),
    COMMETHOD([dispid(74), helpstring('number of nodes in the collection'), 'propget'], HRESULT, 'length',
              ( ['out', 'retval'], POINTER(c_int), 'listLength' )),
    COMMETHOD([dispid(76), helpstring('get next node from iterator')], HRESULT, 'nextNode',
              ( ['out', 'retval'], POINTER(POINTER(IXMLDOMNode)), 'nextItem' )),
    COMMETHOD([dispid(77), helpstring('reset the position of iterator')], HRESULT, 'Reset'),
    COMMETHOD([dispid(-4), 'restricted', 'hidden', 'propget'], HRESULT, '_newEnum',
              ( ['out', 'retval'], POINTER(POINTER(IUnknown)), 'ppunk' )),
]
################################################################
## code template for IXMLDOMNodeList implementation
##class IXMLDOMNodeList_Impl(object):
##    @property
##    def item(self, index):
##        'collection of nodes'
##        #return listItem
##
##    @property
##    def length(self):
##        'number of nodes in the collection'
##        #return listLength
##
##    def nextNode(self):
##        'get next node from iterator'
##        #return nextItem
##
##    def Reset(self):
##        'reset the position of iterator'
##        #return
##
##    @property
##    def _newEnum(self):
##        '-no docstring-'
##        #return ppunk
##

class __MIDL_IAdviseSink_0002(Union):
    pass
class _userHBITMAP(Structure):
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
_userCLIPFORMAT._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0001),
]
assert sizeof(_userCLIPFORMAT) == 8, sizeof(_userCLIPFORMAT)
assert alignment(_userCLIPFORMAT) == 4, alignment(_userCLIPFORMAT)
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

_userHBITMAP._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0007),
]
assert sizeof(_userHBITMAP) == 16, sizeof(_userHBITMAP)
assert alignment(_userHBITMAP) == 8, alignment(_userHBITMAP)
__all__ = [ 'EBO_SHOWFRAMES', 'UINT_PTR', 'EXPLORER_BROWSER_OPTIONS',
           'IMoniker', 'IXMLDOMAttribute', 'IImageRecompress',
           'WebWizardHost', '_remoteMETAFILEPICT', '_userHBITMAP',
           'IAccessibilityDockingServiceCallback',
           'TrayBandSiteService', 'IStartMenuPinnedList',
           'IDataObject', 'NODE_NOTATION', 'SIATTRIBFLAGS_ALLITEMS',
           'DocPropShellExtension', 'AlphabeticalCategorizer',
           'IXMLDOMDocumentFragment', 'GPS_EXTRINSICPROPERTIESONLY',
           'IEnumSTATDATA', 'IEnumMoniker', 'EBF_NONE',
           'UNDOCK_REASON', 'INameSpaceTreeControl',
           'IExecuteCommand', 'NODE_ATTRIBUTE', 'PreviousVersions',
           '_FLAGGED_BYTE_BLOB', 'NODE_ENTITY_REFERENCE', 'ICDBurn',
           'GPS_DELAYCREATION', 'LONG_PTR', 'SIATTRIBFLAGS_MASK',
           'EBO_NONE', 'GPS_DEFAULT', 'EBO_NOPERSISTVIEWSTATE',
           'SIGDN_URL', 'IApplicationAssociationRegistrationUI',
           'IShellItem', 'CATSORT_NAME', 'wireFLAG_STGMEDIUM',
           'IBindCtx', 'SIATTRIBFLAGS_AND', 'IXMLDOMNode',
           'tagLOGPALETTE', 'IShellExtInit', 'IXMLDOMDocumentType',
           'IShellBrowser', 'CATEGORY_INFO', '__MIDL_IWinTypes_0007',
           '_userHENHMETAFILE', 'IShellItemArray',
           'NTSCS2_NOSINGLETONAUTOEXPAND', 'GPS_TEMPORARY',
           'StartMenuPin', 'CATINFO_NORMAL', '_userBITMAP',
           'NSTCS2_DISPLAYPADDING', 'DesktopGadget',
           'IAttachmentExecute', 'GPS_MASK_VALID',
           'IRunningObjectTable', 'DESKBANDINFO',
           'ATTACHMENT_ACTION_EXEC', 'IShellView',
           'NSTCGNI_NEXTVISIBLE', 'wirePIDL',
           'GPS_VOLATILEPROPERTIES', 'UR_MONITOR_DISCONNECT',
           'SIATTRIBFLAGS_OR', 'ATTACHMENT_ACTION',
           'EBO_ALWAYSNAVIGATE', 'EBO_NOWRAPPERWINDOW',
           'NSTCGNI_CHILD', '__MIDL_IAdviseSink_0003',
           'NSTCGNI_FIRSTVISIBLE', 'ICategorizer', 'NODE_ENTITY',
           'SIATTRIBFLAGS', 'ATTACHMENT_ACTION_SAVE',
           'CATINFO_EXPANDED', 'QueryCancelAutoPlay',
           'NamespaceTreeControl', 'CATEGORYINFO_FLAGS',
           'NODE_DOCUMENT_TYPE', 'NODE_CDATA_SECTION',
           '__MIDL_IWinTypes_0008', 'FSCopyHandler',
           'SIATTRIBFLAGS_APPCOMPAT', 'tagRemSNB', 'wireHGLOBAL',
           'NODE_INVALID', '__MIDL_IWinTypes_0009',
           'GPS_HANDLERPROPERTIESONLY', 'tagSTATDATA',
           'IQueryCancelAutoPlay', 'IXMLDOMParseError',
           'CATINFO_NOHEADER', 'IPublishingWizard', 'wireSNB',
           'CDBurn', 'NODE_TEXT', 'wireHMENU', 'NODE_ELEMENT',
           'IXMLDOMCharacterData', '__MIDL_IWinTypes_0004',
           'MergedCategorizer', '_userCLIPFORMAT', 'IXMLDOMDocument',
           'GPS_VOLATILEPROPERTIESONLY', 'FOLDERSETTINGS',
           'NSTCGNI_LASTVISIBLE', 'SIGDN_PARENTRELATIVE',
           'CATINFO_SEPARATE_IMAGES', 'IXMLDOMProcessingInstruction',
           '__MIDL_IAdviseSink_0002', 'INameSpaceTreeControl2',
           'IExplorerBrowserEvents', '_userHMETAFILE', 'IBandSite',
           'IXMLDOMImplementation', 'wireHMONITOR',
           'SIGDN_PARENTRELATIVEFORUI', 'EBO_NOTRAVELLOG', 'IStorage',
           'ApplicationAssociationRegistrationUI', '_userSTGMEDIUM',
           'IVirtualDesktopManager',
           'SIGDN_PARENTRELATIVEFORADDRESSBAR', 'NSTCGNI_NEXT',
           'IDockingWindow', 'IDesktopGadget', 'NSTCGNI_PREVVISIBLE',
           'IPersistStream', 'IStream', 'tagDOMNodeType',
           'CATSORT_DEFAULT', 'IPreviousVersionsInfo',
           'ATTACHMENT_PROMPT_EXEC', 'wireSTGMEDIUM',
           'ImageProperties', 'NSTCS2_DISPLAYPINNEDONLY',
           'ITrayDeskBand', 'IExplorerBrowser',
           'EBO_HTMLSHAREPOINTVIEW', '_STGMEDIUM_UNION',
           'tagOleMenuGroupWidths', 'IWizardExtension',
           'IWebWizardExtension', 'NSTCS2_INTERRUPTNOTIFICATIONS',
           'NSTCS2_SHOWNULLSPACEMENU', 'IXMLDOMText', '_SIGDN',
           '__MIDL_IWinTypes_0003', 'IEnumShellItems',
           'GPS_BESTEFFORT', 'IDropTarget', 'FolderViewHost',
           'ExplorerBrowser', 'ISequentialStream', 'NODE_DOCUMENT',
           'AttachmentServices', 'IXMLDOMNodeList',
           'EBF_NODROPTARGET', '_RemotableHandle', 'IEnumSTATSTG',
           'NODE_PROCESSING_INSTRUCTION', 'InternetPrintOrdering',
           'EBF_SELECTFROMDATAOBJECT', 'CATINFO_SHOWEMPTY',
           'IXMLDOMCDATASection', 'PublishDropTarget',
           'TimeCategorizer', 'IFolderViewHost', 'EBO_NOBORDER',
           'NSTCGNI', 'SIGDN_DESKTOPABSOLUTEEDITING', 'IAdviseSink',
           '__MIDL_IWinTypes_0005', 'GPS_READWRITE', '_userHGLOBAL',
           'ATTACHMENT_PROMPT', 'IAccessibilityDockingService',
           'tagDVTARGETDEVICE', 'GPS_NO_OPLOCK', 'IEnumFORMATETC',
           'CATINFO_NOTCOLLAPSIBLE',
           'NTSCS2_NEVERINSERTNONENUMERATED',
           'SIGDN_PARENTRELATIVEPARSING', 'DOMNodeType',
           'EXPLORER_BROWSER_FILL_FLAGS', 'tagSTATSTG',
           'CATINFO_NOHEADERCOUNT', 'ATTACHMENT_PROMPT_EXEC_OR_SAVE',
           'IENamespaceTreeControl', 'NSTCGNI_PARENT',
           'GPS_EXTRINSICPROPERTIES', 'ATTACHMENT_PROMPT_NONE',
           'IEnumString', 'NODE_DOCUMENT_FRAGMENT',
           'GPS_OPENSLOWITEM', 'IDeskBand', 'tagPALETTEENTRY',
           'GPS_FASTPROPERTIESONLY', 'IXMLDOMElement', 'TrayDeskBand',
           'IXMLDOMEntityReference', 'IOleWindow',
           'CATINFO_SUBSETTED', 'IXMLDOMNamedNodeMap', 'NSTCGNI_PREV',
           'SIGDN_FILESYSPATH', '_tagpropertykey',
           'ATTACHMENT_ACTION_CANCEL', '_userHMETAFILEPICT',
           '__MIDL_IWinTypes_0006', 'tagFORMATETC',
           'wireASYNC_STGMEDIUM', '__MIDL_IWinTypes_0001',
           'AccessibilityDockingService', '_BYTE_BLOB',
           'tagBANDSITEINFO', 'ATTACHMENT_PROMPT_SAVE',
           'ImageRecompress', 'PublishingWizard',
           'SIGDN_DESKTOPABSOLUTEPARSING', 'wireCLIPFORMAT',
           'GPS_PREFERQUERYPROPERTIES', 'ExecuteFolder',
           'CATINFO_COLLAPSED', 'IXMLDOMComment', 'NSTCS2_DEFAULT',
           'SIGDN_PARENTRELATIVEEDITING', 'UR_RESOLUTION_CHANGE',
           'CATSORT_FLAGS', 'SIGDN_NORMALDISPLAY',
           '_userFLAG_STGMEDIUM', 'NSTCSTYLE2', 'CATINFO_HIDDEN',
           '_userHPALETTE', '_GDI_OBJECT', 'VirtualDesktopManager',
           'GETPROPERTYSTOREFLAGS', 'NODE_COMMENT',
           'IShellItemFilter', 'EBO_NAVIGATEONCE']
from comtypes import _check_version; _check_version('')
