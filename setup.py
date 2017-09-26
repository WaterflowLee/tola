from setuptools import find_packages, setup 
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
	def run_tests(self):
		import pytest 
		errno = pytest.main([])
		exit(errno)

setup(
	name="Aiglos",
	packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
	zip_safe=True,
	test_suite="tests",
	tests_require=["pytest"],
	cmdclass={"test": PyTest}
	)