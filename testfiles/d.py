import os.path,subprocess
from subprocess import STDOUT,PIPE


def compile_java(java_file):
    subprocess.check_call(['javac', '-classpath', '.:pdfbox-app-2.0.13.jar', java_file])


def execute_java(java_file, stdin):
    java_class, ext = os.path.splitext(java_file)
    cmd = ['java', '-cp', '.:pdfbox-app-2.0.13.jar', java_class, 'radio_invoice.pdf']
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate(stdin.encode())
    print('This was "' + stdout.decode('utf-8') + '"')


try:
    compile_java('ExtractText.java')
    execute_java('ExtractText.java', 'radio_invoice.pdf')
except Exception as e:
    print("koooo", e)
