# <dataset> template

Part of [`spinalcordtoolbox`](https://github.com/neuropoly/spinalcordtoolbox).


## Usage

1. Clone this repo.

    ```
    git mv src/spinalcordtoolbox/data/dataset src/spinalcordtoolbox/data/${dataset-name} 
    cp ${data_files} src/spinalcordtoolbox/data/${dataset_name} 
    vi setup.py # to edit name= and url=
    vi README.md # to edit the title and *remove* this usage section
    git add .
    git commit
    git remote add origin git@github.com:neuropoly/spinalcordtoolbox-data-${dataset_name}
    git push
    ```

2. Go to https://github.com/neuropoly/spinalcordtoolbox-data-${dataset_name}/releases

    1. Click "Draft Release"
    2. Fill in a version tag. We use [this versioning policy](TODO)
    3. Click "Publish Release"
    4. Wait a few minutes;
    5. Monitor the progress at https://github.com/neuropoly/spinalcordtoolbox-data-${dataset_name}/actions/workflows/release.yml
    6. The release should appear on https://github.com/neuropoly/spinalcordtoolbox-data-${dataset_name}/releases
       with the .tar.gz (sdist) and .whl (wheel) formats attached momentarily.

### Troubleshooting

You can test the repo locally with

```
pip install build &&
python -m build --wheel --sdist &&
pip install dist/*.whl
```

This should give you enough clues hopefully to track down any problems.
