import numpy as np
from absl.logging import info
from absl.testing import absltest
from FrameEventTransform import FrameEventTransform


class FrameEventTransformTest(absltest.TestCase):
    def setUp(self):
        h, w, c = 720, 1280, 3
        self.h, self.w, self.c = h, w, c
        t, x = 2000, 4
        self.long = 8
        self.short = 3
        self.blurs = [np.random.random((h, w, c)) for i in range(self.long)]
        self.sharps = [np.random.random((t, x))*1000 for i in range(self.short)]

    def test_train_transform(self):
        oh, ow = (720, 1280)
        transform = FrameEventTransform((oh, ow))
        blurs, sharps = transform(self.blurs, self.sharps)
        # info(blurs.shape)
        # info(sharps.shape)
        self.assertEqual((self.long,  oh, ow), blurs.shape)
        # self.assertEqual((self.short, self.c, oh, ow), sharps.shape)

    # def test_val_transform(self):
    #     transform = FrameEventTransform()
    #     blurs, sharps = transform(self.blurs, self.sharps)
    #     info(blurs.shape)
    #     info(sharps.shape)
    #     self.assertEqual((self.long, self.c, self.h, self.w), blurs.shape)
    #     self.assertEqual((self.short, self.c, self.h, self.w), sharps.shape)


if __name__ == "__main__":
    absltest.main()
