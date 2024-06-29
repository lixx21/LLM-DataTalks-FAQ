# About

in this project, we will using [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html) and [Mistral.AI](https://mistral.ai/) to build LLM from [DataTalks](https://datatalks.club/) FAQ dataset 

# How To Start

1. install the libraries using `pip install -r requirements.txt`
2. run docker for elastic search using this command `docker run -it --rm --name elasticsearch -p 9200:9200 -p 9300:9300  -e "discovery.type=single-node" -e "xpack.security.enabled=false"  docker.elastic.co/elasticsearch/elasticsearch:8.4.3`
3. run app using `streamlit run app.py`

# App 

![app](https://github.com/lixx21/LLM_DATATALKS_FAQ/blob/master/images/app.png)