import subprocess
import random
import time
import threading
import os
from cryptography.fernet import Fernet
#-----------------------[ RANDOM-UA-CODE ]-----------------------#
def pal():
 rr = random.randint
 rc = random.choice
 uay = f"Mozilla/5.0 (Windows NT {str(rr(1,20))}.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,150))}.0.{str(rr(2000,4999))}.{str(rr(50,200))} Safari/537.36 Maxthon/5.1.5.20"
 return uay
def randomck():
	vivo = random.choice(["U3", "1002T", "C", "1605", "730", "A5", "A54", "a57", "A87","C8818", "EGO", "E1", "E3", "E5", "X21", "X21i", "X2s", "X23","iQOO", "X5Max5", "X5V", "X60t", "X6S", "X7", "X70", "Xplay", "Xshot","Y01", "Y01A", "Y02", "Y02s", "V1", "V11", "V11s", "Y13T", "Nex","S1", "S10", "S11", "S11t", "S12", "S13", "S15", "S15e", "S1PRO","S20", "S21", "S31", "S5", "S6", "S6T", "S7", "S76", "S7e", "S7t", "S7w", "S9", "S9e", "T1", "T1x", "T2", "T2x", "E1","U10","U20","X20", "X1w", "23x", "V77e", "Y613F", "Y628", "X3S","Z1", "Z10", "Z1i", "Z1LITE", "Z1PRO", "Z1x", "Z34"])
	fbpn = random.choice(["com.facebook.katana","com.facebook.orca","messenger-  Android", "com.facebook.lite"])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	  Android_version = str(random.randint(7, 13))
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	fbdv = random.choice(["Vivo Y21", "Vivo Y17s", "Vivo Y02a", "Vivo Y22s"])
	END = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density='+density+',width='+width+',height='+height+'};FBLC/'+fblc+';FBRV/273474118;FBCR/'+fbcr+';FBMF/VIVO;FBBD/VIVO;FBPN/'+fblc+';FBDV/'+str(vivo)+';FBSV/13;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
	uas = 'Mozilla/5.0 (Linux; U;   Android '+str(random.randrange(5,12))+'.13; '+str(fbdv)+' Build/'+str(build)+') '+END
	return uas

def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
mcc = random.choice(['SM-F711B', 'SM-F711N', 'SM-F711U', 'SM-F711U1', 'SM-E025F', 'SM-T575', 'SM-A516V', 'SM-M017F', 'SM-J260GU', 'SM-J260GU', 'SM-J260FU', 'SM-J260MU', 'SM-A716F', 'SM-A716F', 'SM-A716F', 'SM-A7160', 'SM-A716B', 'SM-A716U', 'SM-A716B', 'SM-M115F', 'SM-M115F', 'SM-M115M', 'SM-M115M', 'SM-G988', 'SM-G988U', 'SM-G988U1', 'SM-G9880', 'SM-G988B', 'SM-G988N', 'SM-G988B', 'SM-T927A', 'SM-T920', 'SM-A305F', 'SM-A305FN', 'SM-A305G', 'SM-A305GN', 'SM-A305YN', 'SM-A3050', 'SM-A305N', 'SM-A305GT', 'SM-A105F', 'SM-A105G', 'SM-A105M', 'SM-A105FN', 'SM-A920F', 'SM-A9200', 'SM-A920N', 'SM-A920X', 'SM-N960F', 'SM-N9600', 'SM-N960F', 'SM-N960U', 'SM-N960U1', 'SM-N960N', 'SM-N960W', 'SM-N960X', 'SCV40'])
def trish():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/326.0.134.120;FBBV/285215826;FBDM/{density=2.0,width=1080,height=1920};FBLC/en_NP;FBRV/285811526;FBCR/Azercell;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/'+str(redmi)+';FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U;   Android {random.randint(4,13)}; {redmi}  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
def shishir():
 ios_version = random.choice(["5.13","8.0.0","4.4.4","5.13","10","7.0.0","9","7.1.1","7.1.2","8.1.0","7.0","5.1.1","4.0.4","6.13","11","7.0","5.1","4.4.2","6.0","13","2.3.0","9.13","5.1","7.0","5.1","8.1","12","5"])
 END = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
 ua = random.choice(["[[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"])+END
 return ua    
oppo = random.choice(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
realme = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
infinix = random.choice(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])
samsung = random.choice(['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KO0|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H'])
mamu = requests.get('https://gist.githubusercontent.com/REFAT-156/ce32dac4fd13dc22eb94c9ef5003300f/raw/8b89908acc56beabce9eb329e7873e8e58702515/').text.splitlines()    
def kenovhai():
    facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
      Android_version = f"  Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    fbbv = str(random.randint(10000000, 99999999))
    fbsv = f"{random.uniform(4.0, 10.0):.1f}"
    density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Skitto","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-  Android", "com.facebook.lite"])
    redmi = random.choice(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"])
    model = random.choice(["NEO-AL00","Honor X30","Y550","Y530-U00","Y5 Pro (2017)","Y5 Prime (2018)","Y336-U02","ALA-AN70","DUK-AL20","ATU-L31","MRD-LX2","TRT-LX1","HUAWEI T8833"])
    samsung = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-  Android','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R',
  		  'GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X',
			'GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230',
			'GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838',
			'GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L',
			'GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/'+fban+';FBAV/'+facebook_version+';FBBV/'+fbbv+';FBDM/'+'{density='+density+',width='+str(random.randint(720,1440))+',height='+str(random.randint(1080,2560))+'}'+f';FBLC/'+fblc+';FBRV/279865282;FBCR/'+fbcr+';FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+samsung+';FBSV/'+fbsv+';FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return ua
def sex():
	density = random.choice(['1.0', '1.5', '2.0', '2.25', '2.75', '2.5', '3.0', '3.5', '4.0'])
	width = random.choice(["720", "1080"])
	height = random.choice(["1280", "1440", "1920"])
	END = f'[FBAN/FB4A;FBAV/'+str(random.randint(30,450))+'.0.0.'+str(random.randint(5,70))+'.'+str(random.randint(90,200))+';FBBV/'+str(random.randint(111111111,999999999))+';'+f'[FBAN/FB4A;FBAV/389.0.0.42.111;FBBV/317817216;FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/318410128;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG SHV-E330K;FBSV/5.13;nullFBCA/armeabi-v7a:armeabi;]'
	ua = f'Dalvik/2.1.0 (Linux; U;   Android {random.randint(4,13)}; {random.choice(mamu)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
	return ua
def __UBI___():
    application_version = str(random.randint(111,450))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(80,200))
    application_version_code=str(random.randint(000000000,999999999))
      Android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fbs = random.choice(["com.facebook.katana"])
    ua1 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/'+str(random.randint(000000000,999999999))+';'+f'FBPN/{str(fbs)};FBLC/en_US;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/{random.choice(mamu)};FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    ua2 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=5.25,width=1440,height=2560};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Skitto;FBMF/asus;FBBD/asus;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/7.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.75,width=720,height=1528};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Vodafone;FBMF/motorola;FBBD/motorola;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]'
    ua4 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.25,width=1080,height=2279};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/lifecell;FBMF/motorola;FBBD/motorola;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/9.1;FBOP/1;FBCA/arm64-v8a:;]'
    ua5 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1920};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/TelkomSA;FBMF/samsung;FBBD/samsung;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/7.13;FBOP/19;FBCA/arm64-v8a:;]'
    ua6 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/grameenphone;FBMF/Xiaomi;FBBD/Redmi;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/6.13;FBOP/1;FBCA/arm64-v8a:;]'
    ua7 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.5,width=720,height=1560};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HUAWEI;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/9.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua8 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=4.0,width=1080,height=2340};'+f'FBLC/it_IT;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/9.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua9 = f'Mozilla/5.0 (Linux; U;   Android {str(  Android_version)}.13; {random.choice(mamu)} Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/'+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +';FBBV/'+str(random.randint(1111111,7777777))+';'+f'[FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=4.0,width=1080,height=2412};'+f'FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Nepal Telecom;FBMF/Realme;FBBD/Realme;'+f'FBPN/{str(fbs)};FBDV/{random.choice(mamu)};FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9])  


# Set this variable to True to encrypt, or False to decrypt
ENCRYPT_MODE = True  # Change to False for decryption

# Function to clear the terminal
def clear():
    os.system('clear')

# Function to check if there's internet connectivity
def check_internet():
    try:
        # Ping Google's DNS server to check for internet connection
        output = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception:
        return False

# Function to generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Function to encrypt the code
def encrypt_code():
    key = generate_key()
    cipher_suite = Fernet(key)
    # Read the original Python file
    with open(__file__, 'rb') as file:
        original_file = file.read()

    # Encrypt the file
    encrypted_file = cipher_suite.encrypt(original_file)

    # Save the encrypted file
    with open('your_script_encrypted.py', 'wb') as file:
        file.write(encrypted_file)

    print("Encryption complete. Key saved as 'secret.key'.")

# Function to decrypt the code
def decrypt_code():
    # Load the key for decryption
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    # Read the encrypted file
    with open('your_script_encrypted.py', 'rb') as file:
        encrypted_file = file.read()

    # Decrypt the file
    decrypted_file = cipher_suite.decrypt(encrypted_file)

    # Save the decrypted file
    with open('your_script_decrypted.py', 'wb') as file:
        file.write(decrypted_file)

    print("Decryption complete. Decrypted file saved as 'your_script_decrypted.py'.")

# Loading animation function
def loading_animation(message):
    animation = "|/\|/"
    idx = 0
    while loading:
        print(f"\r{message}... {animation[idx]}", end="")
        idx = (idx + 1) % len(animation)
        time.sleep(13)
    print("\r" + " " * (len(message) + 12) + "\r", end="")  # Clear the line after animation ends

# Main function
if __name__ == "__main__":
    # Start loading animation thread for internet check
    loading = True
    loading_thread = threading.Thread(target=loading_animation, args=("Checking for internet connection",))
    loading_thread.start()

    # Check internet connectivity before proceeding
    if not check_internet():
        loading = False
        loading_thread.join()  # Wait for the loading thread to finish
        print("\033[31mNo internet connection. Please connect to the internet to use this tool.\033[0m")
        exit()

    loading = False
    loading_thread.join()  # Wait for the loading thread to finish

    clear()  # Clear the terminal after checking internet connection

    if ENCRYPT_MODE:
        encrypt_code()
    else:
        if os.path.exists('secret.key') and os.path.exists('your_script_encrypted.py'):
            decrypt_code()
        else:
            print("Decryption files do not exist. Please ensure 'secret.key' and 'your_script_encrypted.py' are present.")
            exit()
#__________________| APPROVAL |__________________#
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
from time import localtime as lt
import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as SIHAB
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
def HOP_M1():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.135.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
        return ua

    # The rest of your script goes here...
    # ANSI escape sequences for colors
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

    def show_banner():
        banner = f"""
      {CYAN}   _______  _______  __   __  __   __  _______  __
        |       ||   _   ||  | |  ||  | |  ||       ||  |
        |    ___||  |_|  ||  |_|  ||  |_|  ||    ___||  |
        |   |___ |       ||       ||       ||   |___ |  |
        |    ___||       ||       ||       ||    ___||__|
        |   |___ |   _   ||   _   ||   _   ||   |___  __
        |_______||__| |__||__| |__||__| |__||_______||__|
        {YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          [☬] {GREEN}DEVELOPER   :   𝕊𝕙𝕠𝕟𝕔𝕙𝕠𝕪𝕠𝕟 𝔹𝕒𝕣𝕦𝕒 𝔸𝕕𝕚𝕣𝕥𝕥𝕒
          [☬] {GREEN}FACEBOOK    :   𝕊𝕙𝕠𝕟𝕔𝕙𝕠𝕪𝕠𝕟 𝔹𝕒𝕣𝕦𝕒 𝔸𝕕𝕚𝕣𝕥𝕥𝕒
          [☬] {GREEN}TOOL TYPE   :   FB-CLONING
          [☬] {GREEN}VERSION     :   RANDOM
          [☬] {GREEN}LOGIN METHOD:   use v.p.n.
        {YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        print(banner)

    def generate_11_digit_number(network_choice):
        # Valid Bangladeshi phone number prefixes based on selected network
        network_prefixes = {
            "1": ["017", "013"],  # Grameenphone
            "2": ["019"],          # Banglalink
            "3": ["015"],          # Teletalk
            "4": ["016"],          # Airtel
            "5": ["018"],          # Robi
            "6": ["017", "019", "015", "016", "018"]  # ALL MIX
        }

        # Choose a random prefix from the selected network
        prefix = random.choice(network_prefixes[network_choice])

        # Generate the rest of the 8 digits
        number = prefix + ''.join(random.choices('0123456789', k=8))

        return number

    def generate_data(num_entries, network_choice):
        entries = []
        for _ in range(num_entries):
            number = generate_11_digit_number(network_choice)
            password = number  # Password is the same as the generated number
            entry = f"+88{number}|{password}"
            entries.append(entry)
            print(f"{GREEN}[SIHAB_💣]➤➤➤[O҉K҉🤍]:➤ {entry}{RESET}")  # Modified print statement
            time.sleep(13)  # Reduced wait time to 13 seconds for faster generation
        return entries

    def save_to_file(filename, data):
        with open(filename, 'w') as file:
            for entry in data:
                file.write(entry + '\n')

    def get_user_choice():
        print("\nChoose a network:")
        print("[01] 𝘎𝘳𝘢𝘮𝘦𝘦𝘯𝘱𝘩𝘰𝘯𝘦")
        print("[02] 𝙱𝚊𝚗𝚐𝚕𝚒𝚗𝚔")
        print("[03] 𝚃𝚎𝚕𝚎𝚝𝚊𝚕𝚔")
        print("[04] 𝙰𝚒𝚛𝚝𝚎𝚕")
        print("[05] 𝚁𝚘𝚋𝚒")
        print("[06] 𝘈𝘓𝘓 𝘔𝘐𝘹")
        print("\nSelect your network (1-6):")

        network_choice = input().strip()

        if network_choice not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{RED}Invalid choice, defaulting to ALL MIX (06).{RESET}")
            network_choice = "6"

        print("\n(1) Generate 900 entries")
        print("(2) Generate 500 entries")
        print("(3) Generate 200 entries")
        print("(4) Enter custom number of entries")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            num_entries = 900
        elif choice == '2':
            num_entries = 500
        elif choice == '3':
            num_entries = 200
        elif choice == '4':
            custom_choice = int(input("Enter the number of entries to generate: "))
            num_entries = custom_choice
        else:
            print(f"{RED}Invalid choice, defaulting to 10 entries.{RESET}")
            num_entries = 10

        return num_entries, network_choice

    # Show the banner
    show_banner()

    # Get user choice for the number of entries and network
    num_entries, network_choice = get_user_choice()

    # Generate the chosen number of entries
    data = generate_data(num_entries, network_choice)

    # Save the data to a file in Termux
    filename = 'SIHAB_ᗪᗩ丅ᗩ.txt'
    save_to_file(filename, data)

    print(f"{YELLOW}\nData saved to {filename}{RESET}")

    print(f"{RED}\ncode by S҉H҉I҉N҉C҉H҉O҉Y҉O҉N҉ ҉B҉A҉R҉U҉A҉ ҉A҉D҉I҉R҉T҉T҉A҉{RESET}")