# CareerAI
CareerAI's repositiory for the job parsing daemon, model calling, and application submission

## Initializing Dependencies in requirements.txt
Firstly install the pipreqs library:
```bash
pip install pipreqs
```
Then utilize the following command after writing a contribution that imports a new dependency:
```bash
python -m pipreqs.pipreqs [folder to be added, use '.' for all] --force (force overwrites previous requirements.txt file)