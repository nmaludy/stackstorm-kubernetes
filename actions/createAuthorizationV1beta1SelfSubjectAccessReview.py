from lib import k8s

from st2actions.runners.pythonrunner import Action


class createAuthorizationV1beta1SelfSubjectAccessReview(Action):

    def run(
            self,
            body,
            config_override=None,
            pretty=None):

        myk8s = k8s.K8sClient(self.config)

        rc = False

        args = {}
        if body is not None:
            args['body'] = body
        else:
            return (False, "body is a required parameter")
        if config_override is not None:
            args['config_override'] = config_override
        if pretty is not None:
            args['pretty'] = pretty
        resp = myk8s.runAction(
            'createAuthorizationV1beta1SelfSubjectAccessReview',
            **args)

        if resp['status'] >= 200 and resp['status'] <= 299:
            rc = True

        return (rc, resp)
