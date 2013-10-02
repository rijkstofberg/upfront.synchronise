from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class UpfrontSynchronise(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import upfront.synchronise
        xmlconfig.file('configure.zcml',
                       upfront.synchronise,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'upfront.synchronise:default')

UPFRONT_SYNCHRONISE_FIXTURE = UpfrontSynchronise()
UPFRONT_SYNCHRONISE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(UPFRONT_SYNCHRONISE_FIXTURE, ),
                       name="UpfrontSynchronise:Integration")