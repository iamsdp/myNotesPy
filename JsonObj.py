
""" Convert Json to python string : When Json obj have no single or double quotes: 
"""
import json 
jsonObj =  [{"pan":{"pan_number": "YAAAA1111A","pan_dmgrphc_dtls": {"name": "ABC Ltd","pan_allot_dt": "17/02/2019","fthr_hsbnd_nm": "test name","dob_doi": "17/02/1982","act_flag": "A","cntct": "1234567891","pan_lnkg_aadhaar": "Y" }}},
           {"pan":{"pan_number": "XAAAA1111A","pan_dmgrphc_dtls": {"name": "ABC Ltd","pan_allot_dt": "17/02/2019","fthr_hsbnd_nm": "test name","dob_doi": "17/02/1982","act_flag": "A","cntct": "1234567891","pan_lnkg_aadhaar": "Y" }}}]

for x in jsonObj:
    # print(x)
    json_obj_str = json.dumps(str(x))
    print(json_obj_str)  #this is python <str>
    
    
""" Convert Json to python string : When Json obj is inside single or double quotes: 
"""    
import json
jsonObj =  '[{"pan":{"pan_number": "AAAAA1111A","pan_dmgrphc_dtls": {"name": "ABC Ltd","pan_allot_dt": "17/02/2019","fthr_hsbnd_nm": "test name","dob_doi": "17/02/1982","act_flag": "A","cntct": "1234567891","pan_lnkg_aadhaar": "Y" }}}]'
json_obj_str = json.loads( json.dumps( jsonObj ))
# print(type(json_obj_str))

