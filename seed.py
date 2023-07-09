from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=8,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="red velvet",
    size="small",
    rating=9,
    image="https://www.rainbownourishments.com/wp-content/uploads/2023/02/vegan-red-velvet-cupcakes-1.jpg"
)

db.session.add_all([c1, c2, c3])
db.session.commit()