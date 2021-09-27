import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.io import shapereader as shpreader 

plt.figure(figsize=(20,10))
ax = plt.axes(projection=ccrs.PlateCarree())

#ax.coastlines()
ax.add_geometries(list(shpreader.Reader("ne_10m_coastline.shp").geometries()), ccrs.PlateCarree(), facecolor="none", edgecolor='black')
ax.set_global()

ax.scatter([133, -97], [-27, 38], color='red', transform=ccrs.PlateCarree())
#  https://docs.google.com/spreadsheets/d/1vXQXZ_nxyLrickJsH46tR_P1FJqgFPW6yvWEq6OxofQ/edit#gid=0


plt.show()
