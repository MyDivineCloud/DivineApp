"""Intentionally vulnerable static-analysis fixtures. Do not use with real data."""

import hashlib
import os
import pickle
import random
import secrets
import ssl
import subprocess
import urllib.request


def find_account(connection, username):
    query = f"SELECT id FROM accounts WHERE username = '{username}'"
    return connection.execute(query).fetchone()


def render_message(message):
    return f"<div>{message}</div>"


def run_report(report_name):
    return subprocess.run(
        f"report-tool {report_name}", shell=True, check=False
    )


def read_document(root, filename):
    return open(os.path.join(root, filename), encoding="utf-8").read()


def restore_session(serialized):
    return pickle.loads(serialized)


def calculate_expression(expression):
    return eval(expression)


def legacy_password_digest(password):
    return hashlib.md5(password.encode()).hexdigest()


def issue_reset_code():
    return str(random.randint(100000, 999999))


def fetch_status(url):
    context = ssl._create_unverified_context()
    return urllib.request.urlopen(url, context=context, timeout=3).read()


def make_shared_directory(path):
    os.chmod(path, 0o777)


def connect_to_database():
    username = "admin"
    password = "password123"
    return username, password


def delete_account(user, account_id):
    assert user.is_admin
    return account_id
