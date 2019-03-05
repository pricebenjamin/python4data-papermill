import papermill as pm

for i in [1, 2, 3]:
    for j in [10, 20, 30]:
        pm.execute_notebook(
            "multiple-params.ipynb",
            f"output-notebooks/hello-papermill-{i}{j}.ipynb",
            parameters=dict(int1=i, int2=j)
        )

