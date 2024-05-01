# Databricks notebook source
# MAGIC %pip install dbdemos

# COMMAND ----------

import dbdemos
#dbdemos.create_cluster('mlops-end2end')

# COMMAND ----------

import dbdemos
dbdemos.list_demos()

# COMMAND ----------

dbdemos.install('lakehouse-iot-platform', overwrite=True)


# COMMAND ----------

dbdemos.install('lakehouse-retail-c360', overwrite=True)

# COMMAND ----------

dbdemos.install('llm-rag-chatbot', overwrite=True)

# COMMAND ----------

#dbdemos.install('lakehouse-iot-platform')
#dbdemos.install('lakehouse-iot-platform', overwrite=True, path='/Repos/kari.ross@databricks.com/sandbox-kari/lakehouse-iot-platform')
#dbdemos.install('uc-01-acl')
#dbdemos.install('llm-dolly-chatbot')
#dbdemos.install('lakehouse-retail-c360')
#dbdemos.install('computer-vision-pcb')
dbdemos.create_cluster('llm-dolly-chatbot')

# COMMAND ----------

dbdemos.install('uc-02-external-location')

# COMMAND ----------

dbdemos.install('uc-03-data-lineage')

# COMMAND ----------

dbdemos.install('uc-04-audit-log')


# COMMAND ----------

dbdemos.install('delta-sharing-airlines', overwrite=True)


# COMMAND ----------

dbdemos.install('dlt-loans', overwrite=True)


# COMMAND ----------


