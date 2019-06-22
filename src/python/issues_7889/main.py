from __future__ import print_function

import pkgutil


def main():
  print(pkgutil.get_data('issues_7889', 'config/prod.config'))


if __name__ == '__main__':
  main()
