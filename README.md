# `${dataset_name}`

Part of [`spinalcordtoolbox`](https://github.com/neuropoly/spinalcordtoolbox).


## Using the Template

1. Go to https://github.com/new and make a repo using this one as its template; name it `spinalcordtoolbox/data-${dataset_name}` where `${dataset_name}` is something descriptive
2. Download the new repo
    
    ```
    git clone git@github.com:spinalcordtoolbox/data-${dataset_name}
    cd data-${dataset_name}
    ```
    
1. Fill with initial metadata
    
    ```
    git mv src/spinalcordtoolbox/data/dataset src/spinalcordtoolbox/data/${dataset-name}
    vi setup.py # to edit name= and url=
    vi README.md # 1. *remove* this Using the Template section
                 # 2. change remaining ${dataset_name}s to the name you picked
    git add -u
    git commit -m "Initial commit"
    ```
    
1. Fill with initial data and upload
    
    ```
    cp ${data_files} src/spinalcordtoolbox/data/${dataset_name} 
    git add .
    git commit
    git push
    ```


## How to update this dataset

1. Edit and commit the files in `src/spinalcordtoolbox/data/`
2. Go to https://github.com/spinalcordtoolbox/data-${dataset_name}/releases

    1. Click "Draft Release"
    2. Fill in a version tag. We use [this versioning policy](TODO)
    3. Click "Publish Release"
    4. Wait a few minutes;
    5. Monitor the progress at https://github.com/spinalcordtoolbox/data-${dataset_name}/actions/workflows/release.yml
    6. The release should appear on https://github.com/spinalcordtoolbox/data-${dataset_name}/releases
       with the .tar.gz (sdist) and .whl (wheel) formats attached momentarily.

### Troubleshooting

You can test the repo locally with

```
pip install build &&
python -m build --wheel --sdist &&
pip install dist/*.whl
```

This should give you enough clues hopefully to track down any problems.