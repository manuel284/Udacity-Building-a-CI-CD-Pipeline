from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def post(self):
        payload = {'CHAS':{'0':0},'RM':{'0':6.575},'TAX':{'0':296.0},'PTRATIO':{'0':15.3},'B':{'0':396.9},'LSTAT':{'0':4.98}}
        self.client.post("/predict", json=payload)      

    @task
    def get(self):
        self.client.get("/")