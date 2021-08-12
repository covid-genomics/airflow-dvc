"""
High-level DVC client for building aced workflows.

@Piotr Styczyński 2021
"""
import datetime
from dataclasses import dataclass
from typing import Any, List, Optional

from airflow.hooks.base import BaseHook
from airflow.models.dag import DAG
from dvc_fs import Client as DVCClient


@dataclass
class DVCCommit:
    """
    Information about the commit created by the DVC operators
    """

    dvc_repo: str  # DVC repo URL
    dvc_repo_name: str  # Same as above
    message: str  # Commit message
    date: datetime.datetime  # Commit time
    dag: DAG  # DAG that triggered this commit
    files: List[str]  # List of modified files
    sha: str  # Commit sha
    commit_url: str  # Commit URL


class DVCHook(DVCClient, BaseHook):
    """
    Interface for all high-level DVC operations.
    For low-level DVC operations please see DVCLocalCli class.
    """

    def __init__(
        self,
        dvc_repo: str,
    ):
        """
        :param dvc_repo: Clone URL for the GIT repo that has DVC configured
        """
        super().__init__(
            dvc_repo,
        )

    def get_conn(self) -> Any:
        return self

    def list_dag_commits(
        self,
        temp_path: Optional[str] = None,
    ) -> List[DVCCommit]:
        """
        Returns list of all commits generated for the given DVC repository.

        :param temp_path: Optional temporary clone path
        :returns: List with commits generated by the DVC operators
        """
        # TODO: Rewrite functionality here using dvc-fs
        return []
