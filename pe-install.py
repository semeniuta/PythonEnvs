import os
import sys
import subprocess
import argparse

PATH = os.path.dirname(os.path.realpath(__file__))


def list_available_groups():

    def is_group_dir(d):
        return d[0] != '.' and os.path.isdir(os.path.join(PATH, d))

    return list(filter(is_group_dir, os.listdir(PATH)))


def conda_install(group_name):

    fname = os.path.join(PATH, group_name, 'conda-reqs.txt')
    if os.path.exists(fname):
        comp = subprocess.run(['conda', 'install', '--yes', '--file', fname])


def pip_install(group_name):

    fname = os.path.join(PATH, group_name, 'pip-reqs.txt')
    if os.path.exists(fname):
        comp = subprocess.run(['pip', 'install', '-r', fname])

def install_group(group_name):

    if group_name not in list_available_groups():
        print('Group {} does not exist'.format(group_name))
        return

    print("Installing packages from", group_name)

    conda_install(group_name)
    pip_install(group_name)


def install_all():

    all_groups = list_available_groups()

    for group_name in all_groups:
        conda_install(group_name)
        pip_install(group_name)


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Install group of packages.')
    arg_parser.add_argument('group')

    args = arg_parser.parse_args()

    if args.group == 'all':
        install_all()
    else:
        install_group(args.group)
