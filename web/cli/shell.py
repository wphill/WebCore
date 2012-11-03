# encoding: utf-8

from __future__ import print_function


def prepare(app):
    """Prepare the shell environment"""
    extensions = [ext.interactive() for ext in app.extensions if hasattr(ext, 'interactive')]
    return dict().update(*extensions)


def run_python(env):
    import code
    code.interact(local=env)


def run_ipython(env):
    import IPython.frontend
    IPython.embed_kernel('__main__', env)


def run_bpython(env):
    pass


def shell(self, interactive=True, run='auto'):
    """Run the shell within the WebCore environment."""
    #env = prepare(self.config.application)
    env = dict()
    interpreters = ['bpython', 'ipython', 'python']
    interpreter = None

    if run != 'auto':
        if run not in interpreters or ('run_' + run) not in globals():
            raise ValueError('Unknown interpreter {0}, use one of: {1}'.format(run, ', '.join(interpreters)))
        interpreters = [run]

    for shell in interpreters:
        try:
            interpreter = globals()['run_' + shell]
        except KeyError:
            pass
        else:
            interpreter(env)
            break

