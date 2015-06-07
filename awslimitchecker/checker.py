"""
awslimitchecker/checker.py

The latest version of this package is available at:
<https://github.com/jantman/awslimitchecker>

################################################################################
Copyright 2015 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of awslimitchecker, also known as awslimitchecker.

    awslimitchecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    awslimitchecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with awslimitchecker.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/pydnstest> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
################################################################################
"""

from awslimitchecker.services import services


class AwsLimitChecker(object):

    def __init__(self):
        self.services = {}
        for sname, cls in services.iteritems():
            self.services[sname] = cls()

    def get_limits(self, service=None):
        """
        Return all :py:class:`~.AwsLimit` objects for the given
        service name, or for all services if ``service`` is None.

        If ``service`` is specified, the returned dict has one element,
        the service name, whose value is a nested dict as described below.

        :param service: the name of one service to return limits for
        :type service: string
        :returns: dict of service name (string) to nested dict
        of limit name (string) to limit (:py:class:`~.AwsLimit`)
        :rtype: dict
        """
        res = {}
        if service is not None:
            return self.services[service].get_limits()
        for sname, cls in self.services.iteritems():
            res[sname] = cls.get_limits()
        return res

    def get_service_names(self):
        """
        Return a list of all known service names

        :returns: list of service names
        :rtype: list
        """
        return sorted(self.services.keys())

    def check_services(self, services=None, region=None):
        """
        Check the specified services.

        :param services: a list of :py:class:`~.service.AwsService`
          names, or None to check all services
        :type services: None or list of strings
        """
        raise NotImplementedError()
