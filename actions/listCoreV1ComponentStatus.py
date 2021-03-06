from lib import k8s

from st2actions.runners.pythonrunner import Action


class listCoreV1ComponentStatus(Action):

    def run(
            self,
            config_override=None,
            fieldSelector=None,
            labelSelector=None,
            pretty=None,
            resourceVersion=None,
            timeoutSeconds=None,
            watch=None):

        myk8s = k8s.K8sClient(self.config)

        rc = False

        args = {}
        if config_override is not None:
            args['config_override'] = config_override
        if fieldSelector is not None:
            args['fieldSelector'] = fieldSelector
        if labelSelector is not None:
            args['labelSelector'] = labelSelector
        if pretty is not None:
            args['pretty'] = pretty
        if resourceVersion is not None:
            args['resourceVersion'] = resourceVersion
        if timeoutSeconds is not None:
            args['timeoutSeconds'] = timeoutSeconds
        if watch is not None:
            args['watch'] = watch
        resp = myk8s.runAction(
            'listCoreV1ComponentStatus',
            **args)

        if resp['status'] >= 200 and resp['status'] <= 299:
            rc = True

        return (rc, resp)
