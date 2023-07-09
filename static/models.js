
BASE_URL = 'http://127.0.0.1:5000/api/cupcakes'



class Cupcake{
    constructor({id,flavor, rating, size, image}){
        this.id=id
        this.flavor=flavor,
        this.rating = rating,
        this.size = size,
        this.image = image
    }
}

class Cupcakes {
    constructor(cupcakes){
        this.cupcakes = cupcakes
    }

    static async getCupcakes(){
        const res = await axios.get(BASE_URL)
        const cupcakes = res.data.cupcakes.map(cupcake => new Cupcake(cupcake))
        return new Cupcakes(cupcakes)
    }

    static async getFilteredCupcakes(flavor_string){
        const res = await axios.get(`${BASE_URL}/${flavor_string}`)
        const cupcakes = res.data.cupcakes.map(cupcake => new Cupcake(cupcake)) 
        return new Cupcakes(cupcakes)
    }

    async addCupcake(data){ 
        const res = await axios.post(BASE_URL, data)
        const cupcake = new Cupcake(res.data.cupcake)
        this.cupcakes.unshift(cupcake)
    }

    async updateCupcake(id,data){
        const res = await axios.patch(`${BASE_URL}/${id}`,data)
        cupcake = this.cupcakes.find(c => c.id === id)
        cupcake.flavour = res.data.cupcake.flavor
        cupcake.rating = res.data.cupcake.rating
        cupcake.flavour = res.data.cupcake.size
        cupcake.flavour = res.data.cupcake.image

        console.log(cupcake)
    }

}