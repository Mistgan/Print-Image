import logging

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

class Print_image(NeuronModule):
    def __init__(self, **kwargs):
        super(Print_image, self).__init__(**kwargs)

        self.media_url = kwargs.get('media_url', None)
        self.size_width = kwargs.get('image_width', 480)
        self.size_height = kwargs.get('image_height', 360)

        # check parameters
        if self._is_parameters_ok():
            

            self.say()

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: MissingParameterException
        """
        if self.media_url is None:
            raise MissingParameterException("Media url parameter required")
        if not isinstance(self.size_width, int):
            raise InvalidParameterException("image_width must be an integer")
        if not isinstance(self.size_height, int):
            raise InvalidParameterException("image_height must be an integer")


        return True
