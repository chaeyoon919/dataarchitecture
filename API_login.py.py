#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_service1_result(companies, logger):
    """Get stuff for service 1.

    :param companies: list of companies(names)
    :type companies: list
    :param logger: logger instance
    :type logger: logging.Logger
    :return: {company: {recent: {date: _, value: _}, predicted: {date: _, value: _}}}
    :rtype: dict
    """
    project_root_path = os.getenv("DA_DESIGN_SERVER")
    cfg = myconfig.get_config('{}/share/project.config'.format(project_root_path))
    db_ip = cfg['db']['ip']
    db_port = int(cfg['db']['port'])
    db_name = cfg['db']['name']

    db_client = MongoClient(db_ip, db_port)
    db = db_client[db_name]

    col_company = db[cfg['db']['col_company']]
    col_pred_company_stock = db[cfg['db']['col_company_predicted']]

    result = dict()
    for cname in companies:
        result[cname] = dict()
        result[cname]['recent'] = dict()
        result[cname]['predicted'] = dict()
        doc_company = col_company.find_one({"name": cname})
        if not doc_company:
            db_client.close()
            continue
        if doc_company['company_stock']:
            result[cname]['recent'] = list(doc_company['company_stock'])[-1]
        doc_pred_stock = col_pred_company_stock.find_one({'Company': doc_company['_id']})
        if not doc_pred_stock:
            db_client.close()
            continue
        preds = doc_pred_stock['company_stock']
        if not preds:
            db_client.close()
            continue
        result[cname]['predicted'] = preds[-1]

    db_client.close()
    return result


# In[2]:


def get_service2_result(company, logger):
    """ Get stuff for service 2.

    :param company: company name
    :type company: str
    :param logger: logger instance
    :type logger: logging.Logger
    :return: {similar_list: [(company_name, score), ...]}
    :rtype: dict
    """
    project_root_path = os.getenv("DA_DESIGN_SERVER")
    cfg = myconfig.get_config('{}/share/project.config'.format(project_root_path))
    db_ip = cfg['db']['ip']
    db_port = int(cfg['db']['port'])
    db_name = cfg['db']['name']

    db_client = MongoClient(db_ip, db_port)
    db = db_client[db_name]

    col_company = db[cfg['db']['col_company']]
    col_similar_company_list = db[cfg['db']['col_company_similar_list']]

    result = dict()
    doc_company = col_company.find_one({'name': company})
    if not doc_company:
        db_client.close()
        return result

    doc_sims = col_similar_company_list.find_one({'Company': doc_company['_id']})
    if not doc_sims:
        db_client.close()
        return result

    tmp_result = doc_sims['similar_list']
    if not tmp_result:
        db_client.close()
        return result

    db_client.close()
    result['similar_list'] = tmp_result
    return result


# In[ ]:




