

import argparse
import json
import random
from datetime import datetime
from uuid import uuid4

from confluent_kafka import Producer
from faker import Faker