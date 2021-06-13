#!/usr/bin/env python
# coding: utf-8

# In[1]:


@app.route('/services', methods=["POST"])
def services():
    """API function of services.

    Specification can be found in `API.md` file.

    :return: JSON serialized string containing the result with session_id
    :rtype: str
    """
    session_id = request.json.get('session_id')
    request_type = request.json.get('request_type')
    loggers['service'].info('{}: service with request type = {}'.format(
        session_id, request_type))

    ret = {"result": None,
        "msg": ""}

    if request_type not in ['service1', 'service2']:
        msg = '{}: Invalid request type = {}'.format(
                session_id, request_type)
        loggers['service'].error(msg)
        ret['result'] = False
        ret['msg'] = msg
        return ret

    what_time_is_it = datetime.datetime.now()
    doc_user = user.check_session(session_id,
            what_time_is_it.timestamp())
    if not doc_user:
        msg = '{}: Invalid session'.format(session_id)
        loggers['service'].error(msg)
        ret['result'] = False
        ret['msg'] = msg
        return ret

    if request_type == 'service1':
        favorites = user.get_favorite(doc_user, loggers['service'])
        ret['msg'] = mymodel.get_service1_result(favorites, loggers['service'])
        ret['result'] = True
    elif request_type == 'service2':
        company_name = request.json.get('company_name')
        ret['msg'] = mymodel.get_service2_result(company_name, loggers['service'])
        ret['result'] = True

    loggers['service'].info('{}: service result = {}'.format(
        session_id, ret))
    return ret

