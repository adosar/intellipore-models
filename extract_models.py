import glob

import torch

datasets = [
    'hmof', 'hmofheat', 'cof', 'ppn',
    'zeolite', 'c3h6c3h8coremof', 'ch4n2',
]

ds_tasks = {
    ds: [i.split('-to_')[-1] for i in glob.glob(f'checkpoints/{ds}/*')]
    for ds in datasets
}

for ds in ds_tasks.keys():
    key = 5000 if ds == 'hmofheat' else 'None'
    for task in ds_tasks[ds]:
        ckpt_path = f'checkpoints/{ds}/from_experiments_pretrain_early_pretrain_lightning_logs_version_0_checkpoints_best.ckpt-to_{task}/{key}/lightning_logs/version_0/checkpoints/best.ckpt'
        ckpt = torch.load(ckpt_path, weights_only=False)
        params = {k.removeprefix('model.'): v for k, v in ckpt['state_dict'].items() if k.startswith('model.')}
        torch.save(params, f'finetuned_models/{ds}_{task}.ckpt')
