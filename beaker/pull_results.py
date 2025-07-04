from typing import List
from beaker import Experiment, Job, Beaker, Experiment # needs beaker<=2


def gather_experiments(author_list, workspace_name, limit=2000) -> List[Experiment]:
    """ Gather all jobs """
    beaker = Beaker.from_env()
    experiments = []

    # Nice bookkeeping to see how many failed per author - a good gut check, if nothing else
    num_author_exps = {}
    for author in author_list:
        num_author_exps[author] = 0

    print(f'Pulling experiments from "{workspace_name}" for author(s) {author_list}...')
    exps = beaker.workspace.experiments(
        workspace=workspace_name, 
        limit=limit
    )
    
    for exp in exps:
        author = exp.author.name

        # filter by author
        if author not in author_list:
            continue

        experiments.append(exp)
        num_author_exps[author] += 1

    return experiments


def get_results(experiments: List[Experiment]):
    results: List[dict] = []

    for experiment in experiments:
        jobs: List[Job] = experiment.jobs

        for job in jobs:
            result: dict = job.execution_results

            if result is not None:
                results += [result]

    return results

def main():
    author = 'davidh'
    workspace = 'ai2/olmo-3-evals'
    limit = 500

    experiments: List[Experiment] = gather_experiments(
        author_list=[author],
        workspace_name=workspace,
        limit=limit
    )

    experiments = [exp for exp in experiments if 'vllm' in exp.name]

    print(get_results(experiments))


if __name__ == '__main__':
    main()