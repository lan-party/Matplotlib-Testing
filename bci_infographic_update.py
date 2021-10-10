import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cartopy.crs as ccrs
from cartopy.io import shapereader as shpreader 

# Scraping
resp = str(requests.get("https://bciwiki.org/index.php/Category:Companies").content)
resp = resp.split("</th></tr>")[1]
resp = resp.split("</tbody></table>")[0]
resp = resp.split("</td></tr>")

companyTimeline = [] 
countries = {'CS': {'value': 0, 'location': [45, 20]}, 'UK': {'value': 0, 'location': [51, 0]}, 'AF': {'value': 0, 'location': [33, 65]}, 'AL': {'value': 0, 'location': [41, 20]}, 'DZ': {'value': 0, 'location': [28, 3]}, 'AS': {'value': 0, 'location': [-14.3333, -170]}, 'AD': {'value': 0, 'location': [42.5, 1.6]}, 'AO': {'value': 0, 'location': [-12.5, 18.5]}, 'AI': {'value': 0, 'location': [18.25, -63.1667]}, 'AQ': {'value': 0, 'location': [-90, 0]}, 'AG': {'value': 0, 'location': [17.05, -61.8]}, 'AR': {'value': 0, 'location': [-34, -64]}, 'AM': {'value': 0, 'location': [40, 45]}, 'AW': {'value': 0, 'location': [12.5, -69.9667]}, 'AU': {'value': 0, 'location': [-27, 133]}, 'AT': {'value': 0, 'location': [47.3333, 13.3333]}, 'AZ': {'value': 0, 'location': [40.5, 47.5]}, 'BS': {'value': 0, 'location': [24.25, -76]}, 'BH': {'value': 0, 'location': [26, 50.55]}, 'BD': {'value': 0, 'location': [24, 90]}, 'BB': {'value': 0, 'location': [13.1667, -59.5333]}, 'BY': {'value': 0, 'location': [53, 28]}, 'BE': {'value': 0, 'location': [50.8333, 4]}, 'BZ': {'value': 0, 'location': [17.25, -88.75]}, 'BJ': {'value': 0, 'location': [9.5, 2.25]}, 'BM': {'value': 0, 'location': [32.3333, -64.75]}, 'BT': {'value': 0, 'location': [27.5, 90.5]}, 'BO': {'value': 0, 'location': [-17, -65]}, 'BA': {'value': 0, 'location': [44, 18]}, 'BW': {'value': 0, 'location': [-22, 24]}, 'BV': {'value': 0, 'location': [-54.4333, 3.4]}, 'BR': {'value': 0, 'location': [-10, -55]}, 'IO': {'value': 0, 'location': [-6, 71.5]}, 'BN': {'value': 0, 'location': [4.5, 114.6667]}, 'BG': {'value': 0, 'location': [43, 25]}, 'BF': {'value': 0, 'location': [13, -2]}, 'BI': {'value': 0, 'location': [-3.5, 30]}, 'KH': {'value': 0, 'location': [13, 105]}, 'CM': {'value': 0, 'location': [6, 12]}, 'CA': {'value': 0, 'location': [60, -95]}, 'CV': {'value': 0, 'location': [16, -24]}, 'KY': {'value': 0, 'location': [19.5, -80.5]}, 'CF': {'value': 0, 'location': [7, 21]}, 'TD': {'value': 0, 'location': [15, 19]}, 'CL': {'value': 0, 'location': [-30, -71]}, 'CN': {'value': 0, 'location': [35, 105]}, 'CX': {'value': 0, 'location': [-10.5, 105.6667]}, 'CC': {'value': 0, 'location': [-12.5, 96.8333]}, 'CO': {'value': 0, 'location': [4, -72]}, 'KM': {'value': 0, 'location': [-12.1667, 44.25]}, 'CG': {'value': 0, 'location': [-1, 15]}, 'CD': {'value': 0, 'location': [0, 25]}, 'CK': {'value': 0, 'location': [-21.2333, -159.7667]}, 'CR': {'value': 0, 'location': [10, -84]}, 'CI': {'value': 0, 'location': [8, -5]}, 'HR': {'value': 0, 'location': [45.1667, 15.5]}, 'CU': {'value': 0, 'location': [21.5, -80]}, 'CY': {'value': 0, 'location': [35, 33]}, 'CZ': {'value': 0, 'location': [49.75, 15.5]}, 'DK': {'value': 0, 'location': [56, 10]}, 'DJ': {'value': 0, 'location': [11.5, 43]}, 'DM': {'value': 0, 'location': [15.4167, -61.3333]}, 'DO': {'value': 0, 'location': [19, -70.6667]}, 'EC': {'value': 0, 'location': [-2, -77.5]}, 'EG': {'value': 0, 'location': [27, 30]}, 'SV': {'value': 0, 'location': [13.8333, -88.9167]}, 'GQ': {'value': 0, 'location': [2, 10]}, 'ER': {'value': 0, 'location': [15, 39]}, 'EE': {'value': 0, 'location': [59, 26]}, 'ET': {'value': 0, 'location': [8, 38]}, 'FK': {'value': 0, 'location': [-51.75, -59]}, 'FO': {'value': 0, 'location': [62, -7]}, 'FJ': {'value': 0, 'location': [-18, 175]}, 'FI': {'value': 0, 'location': [64, 26]}, 'FR': {'value': 0, 'location': [46, 2]}, 'GF': {'value': 0, 'location': [4, -53]}, 'PF': {'value': 0, 'location': [-15, -140]}, 'TF': {'value': 0, 'location': [-43, 67]}, 'GA': {'value': 0, 'location': [-1, 11.75]}, 'GM': {'value': 0, 'location': [13.4667, -16.5667]}, 'GE': {'value': 0, 'location': [42, 43.5]}, 'DE': {'value': 0, 'location': [51, 9]}, 'GH': {'value': 0, 'location': [8, -2]}, 'GI': {'value': 0, 'location': [36.1833, -5.3667]}, 'GR': {'value': 0, 'location': [39, 22]}, 'GL': {'value': 0, 'location': [72, -40]}, 'GD': {'value': 0, 'location': [12.1167, -61.6667]}, 'GP': {'value': 0, 'location': [16.25, -61.5833]}, 'GU': {'value': 0, 'location': [13.4667, 144.7833]}, 'GT': {'value': 0, 'location': [15.5, -90.25]}, 'GG': {'value': 0, 'location': [49.5, -2.56]}, 'GN': {'value': 0, 'location': [11, -10]}, 'GW': {'value': 0, 'location': [12, -15]}, 'GY': {'value': 0, 'location': [5, -59]}, 'HT': {'value': 0, 'location': [19, -72.4167]}, 'HM': {'value': 0, 'location': [-53.1, 72.5167]}, 'VA': {'value': 0, 'location': [41.9, 12.45]}, 'HN': {'value': 0, 'location': [15, -86.5]}, 'HK': {'value': 0, 'location': [22.25, 114.1667]}, 'HU': {'value': 0, 'location': [47, 20]}, 'IS': {'value': 0, 'location': [65, -18]}, 'IN': {'value': 0, 'location': [20, 77]}, 'ID': {'value': 0, 'location': [-5, 120]}, 'IR': {'value': 0, 'location': [32, 53]}, 'IQ': {'value': 0, 'location': [33, 44]}, 'IE': {'value': 0, 'location': [53, -8]}, 'IM': {'value': 0, 'location': [54.23, -4.55]}, 'IL': {'value': 0, 'location': [31.5, 34.75]}, 'IT': {'value': 0, 'location': [42.8333, 12.8333]}, 'JM': {'value': 0, 'location': [18.25, -77.5]}, 'JP': {'value': 0, 'location': [36, 138]}, 'JE': {'value': 0, 'location': [49.21, -2.13]}, 'JO': {'value': 0, 'location': [31, 36]}, 'KZ': {'value': 0, 'location': [48, 68]}, 'KE': {'value': 0, 'location': [1, 38]}, 'KI': {'value': 0, 'location': [1.4167, 173]}, 'KP': {'value': 0, 'location': [40, 127]}, 'KR': {'value': 0, 'location': [37, 127.5]}, 'KW': {'value': 0, 'location': [29.3375, 47.6581]}, 'KG': {'value': 0, 'location': [41, 75]}, 'LA': {'value': 0, 'location': [18, 105]}, 'LV': {'value': 0, 'location': [57, 25]}, 'LB': {'value': 0, 'location': [33.8333, 35.8333]}, 'LS': {'value': 0, 'location': [-29.5, 28.5]}, 'LR': {'value': 0, 'location': [6.5, -9.5]}, 'LY': {'value': 0, 'location': [25, 17]}, 'LI': {'value': 0, 'location': [47.1667, 9.5333]}, 'LT': {'value': 0, 'location': [56, 24]}, 'LU': {'value': 0, 'location': [49.75, 6.1667]}, 'MO': {'value': 0, 'location': [22.1667, 113.55]}, 'MK': {'value': 0, 'location': [41.8333, 22]}, 'MG': {'value': 0, 'location': [-20, 47]}, 'MW': {'value': 0, 'location': [-13.5, 34]}, 'MY': {'value': 0, 'location': [2.5, 112.5]}, 'MV': {'value': 0, 'location': [3.25, 73]}, 'ML': {'value': 0, 'location': [17, -4]}, 'MT': {'value': 0, 'location': [35.8333, 14.5833]}, 'MH': {'value': 0, 'location': [9, 168]}, 'MQ': {'value': 0, 'location': [14.6667, -61]}, 'MR': {'value': 0, 'location': [20, -12]}, 'MU': {'value': 0, 'location': [-20.2833, 57.55]}, 'YT': {'value': 0, 'location': [-12.8333, 45.1667]}, 'MX': {'value': 0, 'location': [23, -102]}, 'FM': {'value': 0, 'location': [6.9167, 158.25]}, 'MD': {'value': 0, 'location': [47, 29]}, 'MC': {'value': 0, 'location': [43.7333, 7.4]}, 'MN': {'value': 0, 'location': [46, 105]}, 'ME': {'value': 0, 'location': [42, 19]}, 'MS': {'value': 0, 'location': [16.75, -62.2]}, 'MA': {'value': 0, 'location': [32, -5]}, 'MZ': {'value': 0, 'location': [-18.25, 35]}, 'MM': {'value': 0, 'location': [22, 98]}, 'NA': {'value': 0, 'location': [-22, 17]}, 'NR': {'value': 0, 'location': [-0.5333, 166.9167]}, 'NP': {'value': 0, 'location': [28, 84]}, 'NL': {'value': 0, 'location': [52.5, 5.75]}, 'AN': {'value': 0, 'location': [12.25, -68.75]}, 'NC': {'value': 0, 'location': [-21.5, 165.5]}, 'NZ': {'value': 0, 'location': [-41, 174]}, 'NI': {'value': 0, 'location': [13, -85]}, 'NE': {'value': 0, 'location': [16, 8]}, 'NG': {'value': 0, 'location': [10, 8]}, 'NU': {'value': 0, 'location': [-19.0333, -169.8667]}, 'NF': {'value': 0, 'location': [-29.0333, 167.95]}, 'MP': {'value': 0, 'location': [15.2, 145.75]}, 'NO': {'value': 0, 'location': [62, 10]}, 'OM': {'value': 0, 'location': [21, 57]}, 'PK': {'value': 0, 'location': [30, 70]}, 'PW': {'value': 0, 'location': [7.5, 134.5]}, 'PS': {'value': 0, 'location': [32, 35.25]}, 'PA': {'value': 0, 'location': [9, -80]}, 'PG': {'value': 0, 'location': [-6, 147]}, 'PY': {'value': 0, 'location': [-23, -58]}, 'PE': {'value': 0, 'location': [-10, -76]}, 'PH': {'value': 0, 'location': [13, 122]}, 'PN': {'value': 0, 'location': [-24.7, -127.4]}, 'PL': {'value': 0, 'location': [52, 20]}, 'PT': {'value': 0, 'location': [39.5, -8]}, 'PR': {'value': 0, 'location': [18.25, -66.5]}, 'QA': {'value': 0, 'location': [25.5, 51.25]}, 'RE': {'value': 0, 'location': [-21.1, 55.6]}, 'RO': {'value': 0, 'location': [46, 25]}, 'RU': {'value': 0, 'location': [60, 100]}, 'RW': {'value': 0, 'location': [-2, 30]}, 'SH': {'value': 0, 'location': [-15.9333, -5.7]}, 'KN': {'value': 0, 'location': [17.3333, -62.75]}, 'LC': {'value': 0, 'location': [13.8833, -61.1333]}, 'PM': {'value': 0, 'location': [46.8333, -56.3333]}, 'VC': {'value': 0, 'location': [13.25, -61.2]}, 'WS': {'value': 0, 'location': [-13.5833, -172.3333]}, 'SM': {'value': 0, 'location': [43.7667, 12.4167]}, 'ST': {'value': 0, 'location': [1, 7]}, 'SA': {'value': 0, 'location': [25, 45]}, 'SN': {'value': 0, 'location': [14, -14]}, 'RS': {'value': 0, 'location': [44, 21]}, 'SC': {'value': 0, 'location': [-4.5833, 55.6667]}, 'SL': {'value': 0, 'location': [8.5, -11.5]}, 'SG': {'value': 0, 'location': [1.3667, 103.8]}, 'SK': {'value': 0, 'location': [48.6667, 19.5]}, 'SI': {'value': 0, 'location': [46, 15]}, 'SB': {'value': 0, 'location': [-8, 159]}, 'SO': {'value': 0, 'location': [10, 49]}, 'ZA': {'value': 0, 'location': [-29, 24]}, 'GS': {'value': 0, 'location': [-54.5, -37]}, 'SS': {'value': 0, 'location': [8, 30]}, 'ES': {'value': 0, 'location': [40, -4]}, 'LK': {'value': 0, 'location': [7, 81]}, 'SD': {'value': 0, 'location': [15, 30]}, 'SR': {'value': 0, 'location': [4, -56]}, 'SJ': {'value': 0, 'location': [78, 20]}, 'SZ': {'value': 0, 'location': [-26.5, 31.5]}, 'SE': {'value': 0, 'location': [62, 15]}, 'CH': {'value': 0, 'location': [47, 8]}, 'SY': {'value': 0, 'location': [35, 38]}, 'TW': {'value': 0, 'location': [23.5, 121]}, 'TJ': {'value': 0, 'location': [39, 71]}, 'TZ': {'value': 0, 'location': [-6, 35]}, 'TH': {'value': 0, 'location': [15, 100]}, 'TL': {'value': 0, 'location': [-8.55, 125.5167]}, 'TG': {'value': 0, 'location': [8, 1.1667]}, 'TK': {'value': 0, 'location': [-9, -172]}, 'TO': {'value': 0, 'location': [-20, -175]}, 'TT': {'value': 0, 'location': [11, -61]}, 'TN': {'value': 0, 'location': [34, 9]}, 'TR': {'value': 0, 'location': [39, 35]}, 'TM': {'value': 0, 'location': [40, 60]}, 'TC': {'value': 0, 'location': [21.75, -71.5833]}, 'TV': {'value': 0, 'location': [-8, 178]}, 'UG': {'value': 0, 'location': [1, 32]}, 'UA': {'value': 0, 'location': [49, 32]}, 'AE': {'value': 0, 'location': [24, 54]}, 'GB': {'value': 0, 'location': [54, -2]}, 'US': {'value': 0, 'location': [38, -97]}, 'UM': {'value': 0, 'location': [19.2833, 166.6]}, 'UY': {'value': 0, 'location': [-33, -56]}, 'UZ': {'value': 0, 'location': [41, 64]}, 'VU': {'value': 0, 'location': [-16, 167]}, 'VE': {'value': 0, 'location': [8, -66]}, 'VN': {'value': 0, 'location': [16, 106]}, 'VG': {'value': 0, 'location': [18.5, -64.5]}, 'VI': {'value': 0, 'location': [18.3333, -64.8333]}, 'WF': {'value': 0, 'location': [-13.3, -176.2]}, 'EH': {'value': 0, 'location': [24.5, -13]}, 'YE': {'value': 0, 'location': [15, 48]}, 'ZM': {'value': 0, 'location': [-15, 30]}, 'ZW': {'value': 0, 'location': [-20, 30]}}
applicationCategories = {'Clinical': 0, 'RC/UI': 0, ' Subjective Measurement': 0, ' Motor-Sensory Augmentation': 0, 'Wetwear Computing': 0} #
bciCategories = {'Open-Loop Efferent BCI': 0, 'Open-Loop Afferent BCI': 0, 'Closed-Loop Efferent BCI': 0, 'Closed-Loop Afferent BCI': 0, 'Bidirectional Afferent Closed-Loop BCI': 0} #
neuroimagingTechniques = {'NIRS': 0, 'EEG': 0, 'ECG': 0, 'EMG': 0, 'fMRI': 0, 'fNIRS': 0, 'fUS': 0, 'iEEG': 0, 'MEG': 0, 'MRI': 0, 'Optogenetics': 0, 'PET': 0} #
neurostimulationTechniques = {'FUS': 0, 'TENS': 0, 'CES': 0, 'DBS': 0, 'EBS': 0, 'EMS': 0, 'Microstimulation': 0, 'Optogenetics': 0, 'PNS': 0, 'SCS': 0, 'tACS': 0, 'tDCS': 0, 'tES': 0, 'TFS': 0, 'tFUS': 0, 'TMS': 0, 'tPCS': 0, 'tRNS': 0, 'VNS': 0}
noninvasiveHardware = {'True': 0, 'False': 0} 
invasiveHardware = {'True': 0, 'False': 0} 
endUserSoftware = {'True': 0, 'False': 0} 
developmentPlatform = {'True': 0, 'False': 0} #
frames = {}

for a in range(0, len(resp)-1):
    companyName = resp[a].split("</a>")[0]
    companyName = companyName.split(">")[-1]
    companyFounding = resp[a].split("<td>")[7]
    companyFounding = companyFounding.split("\\n")[0]
    companyTimeline += [[companyName, companyFounding]]
    companyTimeline.sort(key=lambda x:x[1])
for a in range(0, len(companyTimeline)-1):
    if companyTimeline[a][1] not in frames:
        frames[companyTimeline[a][1]] = {'countries': {'CS': {'value': 0, 'location': [45, 20]}, 'UK': {'value': 0, 'location': [51, 0]}, 'AF': {'value': 0, 'location': [33, 65]}, 'AL': {'value': 0, 'location': [41, 20]}, 'DZ': {'value': 0, 'location': [28, 3]}, 'AS': {'value': 0, 'location': [-14.3333, -170]}, 'AD': {'value': 0, 'location': [42.5, 1.6]}, 'AO': {'value': 0, 'location': [-12.5, 18.5]}, 'AI': {'value': 0, 'location': [18.25, -63.1667]}, 'AQ': {'value': 0, 'location': [-90, 0]}, 'AG': {'value': 0, 'location': [17.05, -61.8]}, 'AR': {'value': 0, 'location': [-34, -64]}, 'AM': {'value': 0, 'location': [40, 45]}, 'AW': {'value': 0, 'location': [12.5, -69.9667]}, 'AU': {'value': 0, 'location': [-27, 133]}, 'AT': {'value': 0, 'location': [47.3333, 13.3333]}, 'AZ': {'value': 0, 'location': [40.5, 47.5]}, 'BS': {'value': 0, 'location': [24.25, -76]}, 'BH': {'value': 0, 'location': [26, 50.55]}, 'BD': {'value': 0, 'location': [24, 90]}, 'BB': {'value': 0, 'location': [13.1667, -59.5333]}, 'BY': {'value': 0, 'location': [53, 28]}, 'BE': {'value': 0, 'location': [50.8333, 4]}, 'BZ': {'value': 0, 'location': [17.25, -88.75]}, 'BJ': {'value': 0, 'location': [9.5, 2.25]}, 'BM': {'value': 0, 'location': [32.3333, -64.75]}, 'BT': {'value': 0, 'location': [27.5, 90.5]}, 'BO': {'value': 0, 'location': [-17, -65]}, 'BA': {'value': 0, 'location': [44, 18]}, 'BW': {'value': 0, 'location': [-22, 24]}, 'BV': {'value': 0, 'location': [-54.4333, 3.4]}, 'BR': {'value': 0, 'location': [-10, -55]}, 'IO': {'value': 0, 'location': [-6, 71.5]}, 'BN': {'value': 0, 'location': [4.5, 114.6667]}, 'BG': {'value': 0, 'location': [43, 25]}, 'BF': {'value': 0, 'location': [13, -2]}, 'BI': {'value': 0, 'location': [-3.5, 30]}, 'KH': {'value': 0, 'location': [13, 105]}, 'CM': {'value': 0, 'location': [6, 12]}, 'CA': {'value': 0, 'location': [60, -95]}, 'CV': {'value': 0, 'location': [16, -24]}, 'KY': {'value': 0, 'location': [19.5, -80.5]}, 'CF': {'value': 0, 'location': [7, 21]}, 'TD': {'value': 0, 'location': [15, 19]}, 'CL': {'value': 0, 'location': [-30, -71]}, 'CN': {'value': 0, 'location': [35, 105]}, 'CX': {'value': 0, 'location': [-10.5, 105.6667]}, 'CC': {'value': 0, 'location': [-12.5, 96.8333]}, 'CO': {'value': 0, 'location': [4, -72]}, 'KM': {'value': 0, 'location': [-12.1667, 44.25]}, 'CG': {'value': 0, 'location': [-1, 15]}, 'CD': {'value': 0, 'location': [0, 25]}, 'CK': {'value': 0, 'location': [-21.2333, -159.7667]}, 'CR': {'value': 0, 'location': [10, -84]}, 'CI': {'value': 0, 'location': [8, -5]}, 'HR': {'value': 0, 'location': [45.1667, 15.5]}, 'CU': {'value': 0, 'location': [21.5, -80]}, 'CY': {'value': 0, 'location': [35, 33]}, 'CZ': {'value': 0, 'location': [49.75, 15.5]}, 'DK': {'value': 0, 'location': [56, 10]}, 'DJ': {'value': 0, 'location': [11.5, 43]}, 'DM': {'value': 0, 'location': [15.4167, -61.3333]}, 'DO': {'value': 0, 'location': [19, -70.6667]}, 'EC': {'value': 0, 'location': [-2, -77.5]}, 'EG': {'value': 0, 'location': [27, 30]}, 'SV': {'value': 0, 'location': [13.8333, -88.9167]}, 'GQ': {'value': 0, 'location': [2, 10]}, 'ER': {'value': 0, 'location': [15, 39]}, 'EE': {'value': 0, 'location': [59, 26]}, 'ET': {'value': 0, 'location': [8, 38]}, 'FK': {'value': 0, 'location': [-51.75, -59]}, 'FO': {'value': 0, 'location': [62, -7]}, 'FJ': {'value': 0, 'location': [-18, 175]}, 'FI': {'value': 0, 'location': [64, 26]}, 'FR': {'value': 0, 'location': [46, 2]}, 'GF': {'value': 0, 'location': [4, -53]}, 'PF': {'value': 0, 'location': [-15, -140]}, 'TF': {'value': 0, 'location': [-43, 67]}, 'GA': {'value': 0, 'location': [-1, 11.75]}, 'GM': {'value': 0, 'location': [13.4667, -16.5667]}, 'GE': {'value': 0, 'location': [42, 43.5]}, 'DE': {'value': 0, 'location': [51, 9]}, 'GH': {'value': 0, 'location': [8, -2]}, 'GI': {'value': 0, 'location': [36.1833, -5.3667]}, 'GR': {'value': 0, 'location': [39, 22]}, 'GL': {'value': 0, 'location': [72, -40]}, 'GD': {'value': 0, 'location': [12.1167, -61.6667]}, 'GP': {'value': 0, 'location': [16.25, -61.5833]}, 'GU': {'value': 0, 'location': [13.4667, 144.7833]}, 'GT': {'value': 0, 'location': [15.5, -90.25]}, 'GG': {'value': 0, 'location': [49.5, -2.56]}, 'GN': {'value': 0, 'location': [11, -10]}, 'GW': {'value': 0, 'location': [12, -15]}, 'GY': {'value': 0, 'location': [5, -59]}, 'HT': {'value': 0, 'location': [19, -72.4167]}, 'HM': {'value': 0, 'location': [-53.1, 72.5167]}, 'VA': {'value': 0, 'location': [41.9, 12.45]}, 'HN': {'value': 0, 'location': [15, -86.5]}, 'HK': {'value': 0, 'location': [22.25, 114.1667]}, 'HU': {'value': 0, 'location': [47, 20]}, 'IS': {'value': 0, 'location': [65, -18]}, 'IN': {'value': 0, 'location': [20, 77]}, 'ID': {'value': 0, 'location': [-5, 120]}, 'IR': {'value': 0, 'location': [32, 53]}, 'IQ': {'value': 0, 'location': [33, 44]}, 'IE': {'value': 0, 'location': [53, -8]}, 'IM': {'value': 0, 'location': [54.23, -4.55]}, 'IL': {'value': 0, 'location': [31.5, 34.75]}, 'IT': {'value': 0, 'location': [42.8333, 12.8333]}, 'JM': {'value': 0, 'location': [18.25, -77.5]}, 'JP': {'value': 0, 'location': [36, 138]}, 'JE': {'value': 0, 'location': [49.21, -2.13]}, 'JO': {'value': 0, 'location': [31, 36]}, 'KZ': {'value': 0, 'location': [48, 68]}, 'KE': {'value': 0, 'location': [1, 38]}, 'KI': {'value': 0, 'location': [1.4167, 173]}, 'KP': {'value': 0, 'location': [40, 127]}, 'KR': {'value': 0, 'location': [37, 127.5]}, 'KW': {'value': 0, 'location': [29.3375, 47.6581]}, 'KG': {'value': 0, 'location': [41, 75]}, 'LA': {'value': 0, 'location': [18, 105]}, 'LV': {'value': 0, 'location': [57, 25]}, 'LB': {'value': 0, 'location': [33.8333, 35.8333]}, 'LS': {'value': 0, 'location': [-29.5, 28.5]}, 'LR': {'value': 0, 'location': [6.5, -9.5]}, 'LY': {'value': 0, 'location': [25, 17]}, 'LI': {'value': 0, 'location': [47.1667, 9.5333]}, 'LT': {'value': 0, 'location': [56, 24]}, 'LU': {'value': 0, 'location': [49.75, 6.1667]}, 'MO': {'value': 0, 'location': [22.1667, 113.55]}, 'MK': {'value': 0, 'location': [41.8333, 22]}, 'MG': {'value': 0, 'location': [-20, 47]}, 'MW': {'value': 0, 'location': [-13.5, 34]}, 'MY': {'value': 0, 'location': [2.5, 112.5]}, 'MV': {'value': 0, 'location': [3.25, 73]}, 'ML': {'value': 0, 'location': [17, -4]}, 'MT': {'value': 0, 'location': [35.8333, 14.5833]}, 'MH': {'value': 0, 'location': [9, 168]}, 'MQ': {'value': 0, 'location': [14.6667, -61]}, 'MR': {'value': 0, 'location': [20, -12]}, 'MU': {'value': 0, 'location': [-20.2833, 57.55]}, 'YT': {'value': 0, 'location': [-12.8333, 45.1667]}, 'MX': {'value': 0, 'location': [23, -102]}, 'FM': {'value': 0, 'location': [6.9167, 158.25]}, 'MD': {'value': 0, 'location': [47, 29]}, 'MC': {'value': 0, 'location': [43.7333, 7.4]}, 'MN': {'value': 0, 'location': [46, 105]}, 'ME': {'value': 0, 'location': [42, 19]}, 'MS': {'value': 0, 'location': [16.75, -62.2]}, 'MA': {'value': 0, 'location': [32, -5]}, 'MZ': {'value': 0, 'location': [-18.25, 35]}, 'MM': {'value': 0, 'location': [22, 98]}, 'NA': {'value': 0, 'location': [-22, 17]}, 'NR': {'value': 0, 'location': [-0.5333, 166.9167]}, 'NP': {'value': 0, 'location': [28, 84]}, 'NL': {'value': 0, 'location': [52.5, 5.75]}, 'AN': {'value': 0, 'location': [12.25, -68.75]}, 'NC': {'value': 0, 'location': [-21.5, 165.5]}, 'NZ': {'value': 0, 'location': [-41, 174]}, 'NI': {'value': 0, 'location': [13, -85]}, 'NE': {'value': 0, 'location': [16, 8]}, 'NG': {'value': 0, 'location': [10, 8]}, 'NU': {'value': 0, 'location': [-19.0333, -169.8667]}, 'NF': {'value': 0, 'location': [-29.0333, 167.95]}, 'MP': {'value': 0, 'location': [15.2, 145.75]}, 'NO': {'value': 0, 'location': [62, 10]}, 'OM': {'value': 0, 'location': [21, 57]}, 'PK': {'value': 0, 'location': [30, 70]}, 'PW': {'value': 0, 'location': [7.5, 134.5]}, 'PS': {'value': 0, 'location': [32, 35.25]}, 'PA': {'value': 0, 'location': [9, -80]}, 'PG': {'value': 0, 'location': [-6, 147]}, 'PY': {'value': 0, 'location': [-23, -58]}, 'PE': {'value': 0, 'location': [-10, -76]}, 'PH': {'value': 0, 'location': [13, 122]}, 'PN': {'value': 0, 'location': [-24.7, -127.4]}, 'PL': {'value': 0, 'location': [52, 20]}, 'PT': {'value': 0, 'location': [39.5, -8]}, 'PR': {'value': 0, 'location': [18.25, -66.5]}, 'QA': {'value': 0, 'location': [25.5, 51.25]}, 'RE': {'value': 0, 'location': [-21.1, 55.6]}, 'RO': {'value': 0, 'location': [46, 25]}, 'RU': {'value': 0, 'location': [60, 100]}, 'RW': {'value': 0, 'location': [-2, 30]}, 'SH': {'value': 0, 'location': [-15.9333, -5.7]}, 'KN': {'value': 0, 'location': [17.3333, -62.75]}, 'LC': {'value': 0, 'location': [13.8833, -61.1333]}, 'PM': {'value': 0, 'location': [46.8333, -56.3333]}, 'VC': {'value': 0, 'location': [13.25, -61.2]}, 'WS': {'value': 0, 'location': [-13.5833, -172.3333]}, 'SM': {'value': 0, 'location': [43.7667, 12.4167]}, 'ST': {'value': 0, 'location': [1, 7]}, 'SA': {'value': 0, 'location': [25, 45]}, 'SN': {'value': 0, 'location': [14, -14]}, 'RS': {'value': 0, 'location': [44, 21]}, 'SC': {'value': 0, 'location': [-4.5833, 55.6667]}, 'SL': {'value': 0, 'location': [8.5, -11.5]}, 'SG': {'value': 0, 'location': [1.3667, 103.8]}, 'SK': {'value': 0, 'location': [48.6667, 19.5]}, 'SI': {'value': 0, 'location': [46, 15]}, 'SB': {'value': 0, 'location': [-8, 159]}, 'SO': {'value': 0, 'location': [10, 49]}, 'ZA': {'value': 0, 'location': [-29, 24]}, 'GS': {'value': 0, 'location': [-54.5, -37]}, 'SS': {'value': 0, 'location': [8, 30]}, 'ES': {'value': 0, 'location': [40, -4]}, 'LK': {'value': 0, 'location': [7, 81]}, 'SD': {'value': 0, 'location': [15, 30]}, 'SR': {'value': 0, 'location': [4, -56]}, 'SJ': {'value': 0, 'location': [78, 20]}, 'SZ': {'value': 0, 'location': [-26.5, 31.5]}, 'SE': {'value': 0, 'location': [62, 15]}, 'CH': {'value': 0, 'location': [47, 8]}, 'SY': {'value': 0, 'location': [35, 38]}, 'TW': {'value': 0, 'location': [23.5, 121]}, 'TJ': {'value': 0, 'location': [39, 71]}, 'TZ': {'value': 0, 'location': [-6, 35]}, 'TH': {'value': 0, 'location': [15, 100]}, 'TL': {'value': 0, 'location': [-8.55, 125.5167]}, 'TG': {'value': 0, 'location': [8, 1.1667]}, 'TK': {'value': 0, 'location': [-9, -172]}, 'TO': {'value': 0, 'location': [-20, -175]}, 'TT': {'value': 0, 'location': [11, -61]}, 'TN': {'value': 0, 'location': [34, 9]}, 'TR': {'value': 0, 'location': [39, 35]}, 'TM': {'value': 0, 'location': [40, 60]}, 'TC': {'value': 0, 'location': [21.75, -71.5833]}, 'TV': {'value': 0, 'location': [-8, 178]}, 'UG': {'value': 0, 'location': [1, 32]}, 'UA': {'value': 0, 'location': [49, 32]}, 'AE': {'value': 0, 'location': [24, 54]}, 'GB': {'value': 0, 'location': [54, -2]}, 'US': {'value': 0, 'location': [38, -97]}, 'UM': {'value': 0, 'location': [19.2833, 166.6]}, 'UY': {'value': 0, 'location': [-33, -56]}, 'UZ': {'value': 0, 'location': [41, 64]}, 'VU': {'value': 0, 'location': [-16, 167]}, 'VE': {'value': 0, 'location': [8, -66]}, 'VN': {'value': 0, 'location': [16, 106]}, 'VG': {'value': 0, 'location': [18.5, -64.5]}, 'VI': {'value': 0, 'location': [18.3333, -64.8333]}, 'WF': {'value': 0, 'location': [-13.3, -176.2]}, 'EH': {'value': 0, 'location': [24.5, -13]}, 'YE': {'value': 0, 'location': [15, 48]}, 'ZM': {'value': 0, 'location': [-15, 30]}, 'ZW': {'value': 0, 'location': [-20, 30]}}, 
                                  'applicationCategories': {'Clinical': 0, 'RC/UI': 0, ' Subjective Measurement': 0, ' Motor-Sensory Augmentation': 0, 'Wetwear Computing': 0}, 
                                  'bciCategories': {'Open-Loop Efferent BCI': 0, 'Open-Loop Afferent BCI': 0, 'Closed-Loop Efferent BCI': 0, 'Closed-Loop Afferent BCI': 0, 'Bidirectional Afferent Closed-Loop BCI': 0},
                                  'neuroimagingTechniques': {'NIRS': 0, 'EEG': 0, 'ECG': 0, 'EMG': 0, 'fMRI': 0, 'fNIRS': 0, 'fUS': 0, 'iEEG': 0, 'MEG': 0, 'MRI': 0, 'Optogenetics': 0, 'PET': 0},
                                  'neurostimulationTechniques': {'FUS': 0, 'TENS': 0, 'CES': 0, 'DBS': 0, 'EBS': 0, 'EMS': 0, 'Microstimulation': 0, 'Optogenetics': 0, 'PNS': 0, 'SCS': 0, 'tACS': 0, 'tDCS': 0, 'tES': 0, 'TFS': 0, 'tFUS': 0, 'TMS': 0, 'tPCS': 0, 'tRNS': 0, 'VNS': 0},
                                  'noninvasiveHardware': {'True': 0, 'False': 0} ,
                                  'invasiveHardware': {'True': 0, 'False': 0} ,
                                  'endUserSoftware': {'True': 0, 'False': 0} ,
                                  'developmentPlatform': {'True': 0, 'False': 0}}

for a in range(0, len(resp)-1):
    companyFounding = resp[a].split("<td>")[7]
    companyFounding = companyFounding.split("\\n")[0]
    
    companyCountry = resp[a].split("<td>")[6]
    companyCountry = companyCountry.split("\\n")[0]
    if companyCountry not in frames[companyFounding]['countries']:
        frames[companyFounding]['countries'].update({companyCountry: {'value': 0}})
    frames[companyFounding]['countries'][companyCountry]['value'] += 1

    if "True" in resp[a].split("<td>")[2]:
        frames[companyFounding]['noninvasiveHardware']['True'] += 1
    else:
        frames[companyFounding]['noninvasiveHardware']['False'] += 1
    
    if "True" in resp[a].split("<td>")[3]:
        frames[companyFounding]['invasiveHardware']['True'] += 1
    else:
        frames[companyFounding]['invasiveHardware']['False'] += 1
    
    if "True" in resp[a].split("<td>")[4]:
        frames[companyFounding]['endUserSoftware']['True'] += 1
    else:
        frames[companyFounding]['endUserSoftware']['False'] += 1
        
    if "True" in resp[a].split("<td>")[5]:
        frames[companyFounding]['developmentPlatform']['True'] += 1
    else:
        frames[companyFounding]['developmentPlatform']['False'] += 1

    applicationCategory = resp[a].split("<td>")[8]
    applicationCategory = applicationCategory.split("\\n")[0]
    for key in frames[companyFounding]['applicationCategories']:
        if key in applicationCategory:
            frames[companyFounding]['applicationCategories'][key] += 1
            
    bciCategory = resp[a].split("<td>")[9]
    bciCategory = bciCategory.split("\\n")[0]
    for key in frames[companyFounding]['bciCategories']:
        if key in bciCategory:
            frames[companyFounding]['bciCategories'][key] += 1
            
    neuroimagingTechnique = resp[a].split("<td>")[10]
    neuroimagingTechnique = neuroimagingTechnique.split("\\n")[0]
    found = False
    for key in frames[companyFounding]['neuroimagingTechniques']:
        if key in neuroimagingTechnique:
            frames[companyFounding]['neuroimagingTechniques'][key] += 1
            found = True
    if not found and neuroimagingTechnique != "":
        neuroimagingTechnique = neuroimagingTechnique.split(">")[1]
        neuroimagingTechnique = neuroimagingTechnique.split("<")[0]
        frames[companyFounding]['neuroimagingTechniques'].update({neuroimagingTechnique: 1})
            
    neurostimulationTechnique = resp[a].split("<td>")[11]
    neurostimulationTechnique = neurostimulationTechnique.split("\\n")[0]
    found = False
    for key in frames[companyFounding]['neurostimulationTechniques']:
        if key in neurostimulationTechnique:
            frames[companyFounding]['neurostimulationTechniques'][key] += 1
            found = True
    if not found and neurostimulationTechnique != "":
        neurostimulationTechnique = neurostimulationTechnique.split(">")[1]
        neurostimulationTechnique = neurostimulationTechnique.split("<")[0]
        frames[companyFounding]['neurostimulationTechniques'].update({neurostimulationTechnique: 1})

# print(noninvasiveHardware)
# print(invasiveHardware)
# print(applicationCategories)
# print(bciCategories)
# print(companyTimeline)
# print(countries)
# print(neuroimagingTechniques)
# print(neurostimulationTechniques)
# print(endUserSoftware)
# print(developmentPlatform)

# Plotting
fig = plt.figure(1)
fig2 = plt.figure(2)
#plt.style.use('dark_background')
plt.style.use('grayscale')
sub1 = fig.add_subplot(321)
sub2 = fig.add_subplot(322)
sub3 = fig.add_subplot(323)
sub4 = fig.add_subplot(324)
sub5 = fig.add_subplot(313)
sub6 = fig2.add_subplot(1,1,1,projection=ccrs.PlateCarree())
fig.tight_layout()
fig.set_size_inches(20, 30)
fig2.set_size_inches(30, 20)


def sortDict(d):
    sorted_dict = {}
    sorted_keys = sorted(d, key=d.get)
    for w in sorted_keys:
        sorted_dict[w] = d[w]
    return sorted_dict


def getCountryLists(c):
    valueslist = []
    lats = []
    longs = []
    for key in c:
        valueslist += [c[key]['value']*80]
        lats += [c[key]['location'][0]]
        longs += [c[key]['location'][1]]
    return valueslist, lats, longs

def animate(i):
    for key in frames[str(i)]['applicationCategories'].keys():
        applicationCategories[key] += frames[str(i)]['applicationCategories'][key]
    for key in frames[str(i)]['bciCategories'].keys():
        bciCategories[key] += frames[str(i)]['bciCategories'][key]
    for key in frames[str(i)]['neuroimagingTechniques'].keys():
        neuroimagingTechniques[key] += frames[str(i)]['neuroimagingTechniques'][key]
    for key in frames[str(i)]['neurostimulationTechniques'].keys():
        neurostimulationTechniques[key] += frames[str(i)]['neurostimulationTechniques'][key]
    
    for key in frames[str(i)]['noninvasiveHardware'].keys():
        noninvasiveHardware[key] += frames[str(i)]['noninvasiveHardware'][key]
    for key in frames[str(i)]['invasiveHardware'].keys():
        invasiveHardware[key] += frames[str(i)]['invasiveHardware'][key]
    for key in frames[str(i)]['endUserSoftware'].keys():
        endUserSoftware[key] += frames[str(i)]['endUserSoftware'][key]
    for key in frames[str(i)]['noninvasiveHardware'].keys():
        developmentPlatform[key] += frames[str(i)]['developmentPlatform'][key]
        
    for key in frames[str(i)]['countries'].keys():
        countries[key]['value'] += frames[str(i)]['countries'][key]['value']
    
    sub1.clear()
    sub1.set_title("Application Categories")
    sub1.tick_params(axis='x', labelrotation=6)
    sub1.bar(list(applicationCategories.keys()), list(applicationCategories.values()))
    sub2.clear()
    sub2.set_title("BCI Categories")
    sub2.tick_params(axis='x', labelrotation=6)
    sub2.bar(list(bciCategories.keys()), list(bciCategories.values()))
    sub3.clear()
    sub3.set_title("Neuroimaging Techniques")
    sub3.tick_params(axis='x', labelrotation=45)
    neuroimagingTechniquesSorted = sortDict(neuroimagingTechniques)
    sub3.bar(list(neuroimagingTechniquesSorted.keys()), list(neuroimagingTechniquesSorted.values()))
    sub4.clear()
    sub4.set_title("Neurostimulation Techniques")
    sub4.tick_params(axis='x', labelrotation=45)
    neurostimulationTechniquesSorted = sortDict(neurostimulationTechniques)
    sub4.bar(list(neurostimulationTechniquesSorted.keys()), list(neurostimulationTechniquesSorted.values()))
    
    sub5.clear()
    sub5.axis('off')
    sub5.scatter([1, 2, 3, 4], [1, 1, 1, 1], s=[noninvasiveHardware["True"]*100, invasiveHardware["True"]*100, endUserSoftware["True"]*100, developmentPlatform["True"]*100])
    sub5.text(1, 1.025+(0.0001*noninvasiveHardware["True"]), "Noninvasive Hardware")
    sub5.text(1.1, 0.975-(0.0001*noninvasiveHardware["True"]), str(noninvasiveHardware["True"]))
    sub5.text(2, 1.025+(0.0001*invasiveHardware["True"]), "Invasive Hardware")
    sub5.text(2.1, 0.975-(0.0001*invasiveHardware["True"]), str(invasiveHardware["True"]))
    sub5.text(3, 1.025+(0.0001*endUserSoftware["True"]), "End-user Software")
    sub5.text(3.1, 0.975-(0.0001*endUserSoftware["True"]), str(endUserSoftware["True"]))
    sub5.text(4, 1.025+(0.0001*developmentPlatform["True"]), "Development Platform")
    sub5.text(4.1, 0.975-(0.0001*developmentPlatform["True"]), str(developmentPlatform["True"]))
    sub5.title.set_text(str(i))
    sub5.title.set_size(40)
    
    valueslist, lats, longs = getCountryLists(countries)
    sub6.clear()
    sub6.add_geometries(list(shpreader.Reader("ne_10m_coastline.shp").geometries()), ccrs.PlateCarree(), facecolor="none", edgecolor='black')
    sub6.set_global()
    sub6.scatter(longs, lats, s=valueslist, color='red', alpha=0.5, transform=ccrs.PlateCarree())
    sub6.title.set_text(str(i))
    sub6.title.set_size(40)

ani = animation.FuncAnimation(fig, animate, interval=500, frames=[int(a) for a in list(frames.keys())])
ani2 = animation.FuncAnimation(fig2, animate, interval=500, frames=[int(a) for a in list(frames.keys())])

plt.show()
#ani.save('bci infographic.gif', writer='imagemagick')
ani2.save('bci infographic2.gif', writer='imagemagick')
