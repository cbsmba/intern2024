from bs4 import BeautifulSoup
import csv

file_name = "음성무극시장.kml"

with open(file_name, 'r', encoding = "utf-8") as f:
        s = BeautifulSoup(f, 'xml')
        content =s.find_all('coordinates')

        coord_result = []
        if len(content) == 1:
            coords_str = content[0].text
            coords_str = coords_str.replace("\n","").replace("\t","")

            coords_list = coords_str.split(" ")

            for coord in coords_list:
                coord_detail = coord.split(",")
                if len(coord_detail) == 3:
                    coord_result.append([coord_detail[1], coord_detail[0]])
                    print(coord_detail)
                    
            #print(coords_str)
            
        else:
            print("파일 점검 필요")
        print(coord_result)

js_code = f''' "{file_name.split('.')[0]}" : [ \n'''

for i in range(len(coord_result)-1):
    temp = f"new kakao.maps.LatLng({coord_result[i][0]}, {coord_result[i][1]} ), \n"
    #print(temp)
    js_code = js_code + temp

js_code = js_code + "],"
print(js_code)
