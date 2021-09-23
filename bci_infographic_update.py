import requests
import matplotlib.pyplot as plt

# Scraping
resp = str(requests.get("https://bciwiki.org/index.php/Category:Companies").content)
resp = resp.split("</th></tr>")[1]
resp = resp.split("</tbody></table>")[0]
resp = resp.split("</td></tr>")

companyTimeline = [] 
countries = {} 
applicationCategories = {'Clinical': 0, 'RC/UI': 0, ' Subjective Measurement': 0, ' Motor-Sensory Augmentation': 0, 'Wetwear Computing': 0} #
bciCategories = {'Open-Loop Efferent BCI': 0, 'Open-Loop Afferent BCI': 0, 'Closed-Loop Efferent BCI': 0, 'Closed-Loop Afferent BCI': 0, 'Bidirectional Afferent Closed-Loop BCI': 0} #
neuroimagingTechniques = {'EEG': 0, 'ECG': 0, 'EMG': 0, 'fMRI': 0, 'fNIRS': 0, 'fUS': 0, 'iEEG': 0, 'MEG': 0, 'MRI': 0, 'Optogenetics': 0, 'PET': 0} #
neurostimulationTechniques = {'CES': 0, 'DBS': 0, 'EBS': 0, 'EMS': 0, 'Microstimulation': 0, 'Optogenetics': 0, 'PNS': 0, 'SCS': 0, 'tACS': 0, 'tDCS': 0, 'tES': 0, 'TFS': 0, 'tFUS': 0, 'TMS': 0, 'tPCS': 0, 'tRNS': 0, 'VNS': 0}
noninvasiveHardware = {'True': 0, 'False': 0} 
invasiveHardware = {'True': 0, 'False': 0} 
endUserSoftware = {'True': 0, 'False': 0} 
developmentPlatform = {'True': 0, 'False': 0} #

for a in range(0, len(resp)-1):
    companyName = resp[a].split("</a>")[0]
    companyName = companyName.split(">")[-1]
    companyFounding = resp[a].split("<td>")[7]
    companyFounding = companyFounding.split("\\n")[0]
    companyTimeline += [[companyName, companyFounding]]
    companyTimeline.sort(key=lambda x:x[1])

    companyCountry = resp[a].split("<td>")[6]
    companyCountry = companyCountry.split("\\n")[0]
    if companyCountry not in countries:
        countries.update({companyCountry: 0})
    countries[companyCountry] += 1

    if "True" in resp[a].split("<td>")[2]:
        noninvasiveHardware['True'] += 1
    else:
        noninvasiveHardware['False'] += 1
    
    if "True" in resp[a].split("<td>")[3]:
        invasiveHardware['True'] += 1
    else:
        invasiveHardware['False'] += 1
    
    if "True" in resp[a].split("<td>")[4]:
        endUserSoftware['True'] += 1
    else:
        endUserSoftware['False'] += 1
        
    if "True" in resp[a].split("<td>")[5]:
        developmentPlatform['True'] += 1
    else:
        developmentPlatform['False'] += 1

    applicationCategory = resp[a].split("<td>")[8]
    applicationCategory = applicationCategory.split("\\n")[0]
    for key in applicationCategories:
        if key in applicationCategory:
            applicationCategories[key] += 1
            
    bciCategory = resp[a].split("<td>")[9]
    bciCategory = bciCategory.split("\\n")[0]
    for key in bciCategories:
        if key in bciCategory:
            bciCategories[key] += 1
            
    neuroimagingTechnique = resp[a].split("<td>")[10]
    neuroimagingTechnique = neuroimagingTechnique.split("\\n")[0]
    for key in neuroimagingTechniques:
        if key in neuroimagingTechnique:
            neuroimagingTechniques[key] += 1
            
    neurostimulationTechnique = resp[a].split("<td>")[11]
    neurostimulationTechnique = neurostimulationTechnique.split("\\n")[0]
    for key in neurostimulationTechniques:
        if key in neurostimulationTechnique:
            neurostimulationTechniques[key] += 1

print(noninvasiveHardware)
print(invasiveHardware)
print(applicationCategories)
print(bciCategories)
print(companyTimeline)
print(countries)
print(neuroimagingTechniques)
print(neurostimulationTechniques)

# Plotting
fig = plt.figure()
#plt.style.use('dark_background')
plt.style.use('grayscale')
sub1 = fig.add_subplot(321)
sub2 = fig.add_subplot(322)
sub3 = fig.add_subplot(323)
sub4 = fig.add_subplot(324)
sub5 = fig.add_subplot(313)
fig.tight_layout()

sub1.set_title("Application Categories")
sub1.tick_params(axis='x', labelrotation=6)
sub1.bar(list(applicationCategories.keys()), list(applicationCategories.values()))
sub2.set_title("BCI Categories")
sub2.tick_params(axis='x', labelrotation=6)
sub2.bar(list(bciCategories.keys()), list(bciCategories.values()))
sub3.set_title("Neuroimaging Techniques")
sub3.tick_params(axis='x', labelrotation=45)
sub3.bar(list(neuroimagingTechniques.keys()), list(neuroimagingTechniques.values()))
sub4.set_title("Neurostimulation Techniques")
sub4.tick_params(axis='x', labelrotation=45)
sub4.bar(list(neurostimulationTechniques.keys()), list(neurostimulationTechniques.values()))

sub5.axis('off')
sub5.scatter([1, 2, 3, 4], [1, 1, 1, 1], s=[noninvasiveHardware["True"]*100, invasiveHardware["True"]*100, endUserSoftware["True"]*100, developmentPlatform["True"]*100])
sub5.text(1, 1.2+(0.001*noninvasiveHardware["True"]), "Noninvasive Hardware")
sub5.text(1.1, 1.14+(0.001*noninvasiveHardware["True"]), str(noninvasiveHardware["True"]))
sub5.text(2, 1.2+(0.001*invasiveHardware["True"]), "Invasive Hardware")
sub5.text(2.1, 1.14+(0.001*invasiveHardware["True"]), str(invasiveHardware["True"]))
sub5.text(3, 1.2+(0.001*endUserSoftware["True"]), "End-user Software")
sub5.text(3.1, 1.14+(0.001*endUserSoftware["True"]), str(endUserSoftware["True"]))
sub5.text(4, 1.2+(0.001*developmentPlatform["True"]), "Development Platform")
sub5.text(4.1, 1.14+(0.001*developmentPlatform["True"]), str(developmentPlatform["True"]))


fig.set_size_inches(20, 15)
plt.savefig("bci_infographic.png")
