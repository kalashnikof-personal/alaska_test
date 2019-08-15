from common import *


class TestAddBear(Common):

    def test_add_bear(self):
        for bear_type in self.ALL_BEAR_TYPES:
            # create new bear
            new_bear = self.generate_bear(bear_type)
            response_add_bear = self.make_request(self.METHOD_POST, payload=json.dumps(asdict(new_bear)))

            # check that response code is correct
            with self.subTest(f"bear_type = {bear_type} Response code = 201"):
                # correct response code here should be 201 according to REST principles
                self.assertEqual(response_add_bear.status_code, 201),
            with self.subTest(f"bear_type = {bear_type} Response body is not empty"):
                self.assertIsNotNone(response_add_bear.json()),

            # check that bear was added correctly
            new_bear.bear_id = response_add_bear.json()
            response_get_bear = self.make_request(id_=new_bear.bear_id)

            for bear_value in self.ALL_BEAR_VALUES:
                with self.subTest(f"bear_type = {bear_type} Check {bear_value} value"):
                    actual = response_get_bear.json()[bear_value]
                    expected = asdict(new_bear)[bear_value]
                    self.assertEqual(actual, expected,
                                     "Actual != expected for {}: {} != {}".format(bear_value, actual, expected))

    def test_add_bear_without_mandatory_value(self):
        for bear_type in self.ALL_BEAR_TYPES:
            for bear_value in self.MANDATORY_BEAR_VALUES:
                # save bears list before the test
                all_bears_before = self.make_request().json()

                # create new bear
                new_bear = self.generate_bear(bear_type)

                # remove one of bear values
                new_bear_dict = asdict(new_bear)
                new_bear_dict.pop(bear_value)

                # try to create new bear
                response_add_bear = self.make_request(self.METHOD_POST, payload=json.dumps(new_bear_dict))

                # check that response is correct
                with self.subTest(
                        f"bear_type = {bear_type} Create bear without {bear_value} value: Response code = 400"):
                    # correct response code here should be 400 according to REST principles
                    self.assertEqual(response_add_bear.status_code, 400)
                with self.subTest(f"bear_type = {bear_type} Create bear without {bear_value} value: Response text"):
                    self.assertEqual(response_add_bear.text, "Error. Pls fill all parameters")

                # check that new bear wasn't added and list of bears did't change
                all_bears_after = self.make_request().json()
                with self.subTest(
                        f"bear_type = {bear_type} Create bear without {bear_value} value: Bear was not added"):
                    self.assertEqual(all_bears_before, all_bears_after)
