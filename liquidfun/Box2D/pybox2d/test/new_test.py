import sys # "hack"
sys.path.append('/home/tbeier/bld/liquidfun/liquidfun/Box2D/python/')
import pybox2d as b2

import unittest
import nose

class TestPyWorld(unittest.TestCase):

    # def test_body_user_data_from_def(self):

    #     world = b2.world((0,-9.81))
    #     body_def = b2.body_def(user_data='dontbeafraid')
    #     body = world.create_dynamic_body(body_def=body_def)

    #     self.assertFalse(body.has_int_user_data)
    #     self.assertTrue(body.has_object_user_data)
    #     self.assertTrue(body.user_data == 'dontbeafraid')
    #     self.assertTrue(body.int_user_data is None)

    #     self.assertFalse(body_def.has_int_user_data)
    #     self.assertTrue(body_def.has_object_user_data)
    #     self.assertTrue(body_def.user_data == 'dontbeafraid')
    #     self.assertTrue(body_def.int_user_data is None)


    #     world = b2.world((0,-9.81))
    #     body_def = b2.body_def(int_user_data=2)
    #     body = world.create_dynamic_body(body_def=body_def)

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertFalse(body.has_object_user_data)
    #     self.assertTrue(body.user_data is None)
    #     self.assertTrue(body.int_user_data == 2)

    #     self.assertTrue(body_def.has_int_user_data)
    #     self.assertFalse(body_def.has_object_user_data)
    #     self.assertTrue(body_def.user_data is None)
    #     self.assertTrue(body_def.int_user_data == 2)

    # def test_body_user_data(self):

    #     world = b2.world((0,-9.81))
    #     body = world.create_dynamic_body()
    #     self.assertFalse(body.has_int_user_data)
    #     self.assertFalse(body.has_object_user_data)
    #     self.assertTrue(body.int_user_data is None)
    #     self.assertTrue(body.user_data is None)

    #     body.int_user_data = -42

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertFalse(body.has_object_user_data)
    #     self.assertTrue(body.int_user_data ==  -42)
    #     self.assertTrue(body.user_data is None)

    #     body.user_data = 'hello'

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertTrue(body.has_object_user_data)
    #     self.assertTrue(body.int_user_data ==  -42)
    #     self.assertTrue(body.user_data == 'hello')

    #     body.int_user_data = 22

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertTrue(body.int_user_data ==  22)
    #     self.assertTrue(body.user_data == 'hello')

    #     body.user_data = (1,2)

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertTrue(body.int_user_data ==  22)
    #     self.assertTrue(body.user_data == (1,2))


    #     body.user_data = None

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertFalse(body.has_object_user_data)
    #     self.assertTrue(body.int_user_data ==  22)
    #     self.assertTrue(body.user_data == None)

    #     body.user_data = 'bla'

    #     self.assertTrue(body.has_int_user_data)
    #     self.assertTrue(body.has_object_user_data)
    #     self.assertTrue(body.int_user_data ==  22)
    #     self.assertTrue(body.user_data == 'bla')

    #     body.int_user_data = None 

    #     self.assertFalse(body.has_int_user_data)
    #     self.assertTrue(body.has_object_user_data)
    #     self.assertTrue(body.user_data == 'bla')

    #     body.user_data = None
    #     self.assertFalse(body.has_int_user_data)
    #     self.assertFalse(body.has_object_user_data)


    def test_joint_user_data(self):

        world = b2.world((0,-9.81))
        body_a = world.create_dynamic_body()
        body_b = world.create_dynamic_body()
        dj = world.create_distance_joint(body_a=body_a, 
                                         body_b=body_b,
                                         int_user_data=42,
                                         user_data='hello')
        self.assertTrue( isinstance(dj, b2.DistanceJoint))
        self.assertTrue(dj.has_int_user_data)
        self.assertTrue(dj.int_user_data ==  42)
        self.assertTrue(dj.user_data == 'hello') 

class TestBodyVector(unittest.TestCase):

    def test_append(self):
        world = b2.world((0,-9.81))
        body = world.create_dynamic_body()
        body_vec = b2.BodyVector()
        body_vec.append(body)
        c = 0
        for body in body_vec:
            c += 1
        self.assertTrue(c == 1)


t = TestBodyVector()
t.test_append()
nose.main()
