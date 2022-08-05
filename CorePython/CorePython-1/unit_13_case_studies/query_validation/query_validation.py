result1 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'splunk',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'SLO', 'status': 'Published', 'comments': [], 'comment': None}
result2 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'splunk',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None}
result3 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'prometheus',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'SLO', 'status': 'Published', 'comments': [], 'comment': None}
result4 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'prometheus',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None}

# print(result4['formType']) # SLO/CTA
# index_str = result1['query']
# print(type(index_str))
# print(index_str)

results = [
    {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'splunk',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'SLO', 'status': 'Published', 'comments': [], 'comment': None},
    {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'splunk',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None},
    {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'prometheus',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'SLO', 'status': 'Published', 'comments': [], 'comment': None},
{'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',
           'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217',
           'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'],
           'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'prometheus',
           'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count',
           'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None}
            ]
# Type
# print(reasults)
# print(type(results))
# for result in results:
#     print(type(result))
#     print("------------------------------")

# Form type
queries =[]
for result in results:
    # print(result['formType']) # SLO/CTA
    form_type = result['formType']
    data_source = result['datasource']
    if form_type == 'SLO' or form_type == 'CTA':
        if data_source == 'prometheus' or data_source == 'splunk':
            tmp_query = result['query']
            # print(result)
            # print(tmp_query)
            if (tmp_query.find('index')>=0) and (tmp_query.find('source')>=0) and (tmp_query.find('eval')>=0): # also cr_dt == today (0 days difference) date_diff (0) -> Today
                # print(result)
                tmp_dict = {'data_source':data_source, 'query':tmp_query}
                queries.append(tmp_dict)
                # print("OK")
            else:
                pass
    print("")
# print(len(queries))

for query in queries:
    if query['data_source']=='splunk':
        print('call splink api')
    elif query['data_source']=='prometheus':
        print('call prometheus api')

# API Call
# api_result stats code 200 # Retrieve
# requests
# print result