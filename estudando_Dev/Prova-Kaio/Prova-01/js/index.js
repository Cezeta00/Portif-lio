const URL = "https://apiintranet.kryptonbpo.com.br/test-dev/exercise-1";
let cars = [];
let motors = [];

function clickSearch() {
  $.ajax({
    url: URL,
    type: "GET",
    success: function (response) {
      cars = response.carros;
      motors = response.motores;

      console.log("clickSearch", cars);
      carOptions();
    },
    error: function (error) {
      console.error(error);
    },
  });
}
function carOptions() {
  let options = "";
  for (let i = 0; i < cars.length; i++) {
    console.log("for", cars[i]);

    options += `
      <option value="${cars[i].id}">${cars[i].modelo.toUpperCase()}</option>`;
  }
  $("#cars")[0].innerHTML = options;
}

function infos() {
  let position = $("#cars").val();
  let carInfo = {};
  let motorInfo = {};
  for (let i = 0; i < cars.length; i++) {
    if (cars[i].id == position) {
      carInfo = cars[i];
    }
  }
  for (i = 0; i < motors.length; i++) {
    if (motors[i].id == carInfo.motor_id) {
      motorInfo = motors[i];
    }
  }
  console.log("carInfo", carInfo, "motorInfo", motorInfo);
  $("#infos")[0].innerHTML = garage(carInfo, motorInfo);
  return {
    car: carInfo,
    motor: motorInfo,
  };
}

//return car selected in garage
function garage(car, motor) {
  let asset = `<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">${car.id}</h5>
    <h4> ${car.modelo}  \nColor:${car.cor} </h4>
    <p class="card-text"> Has an amazing ${motor.cilindros} cylinders in ${motor.posicionamento_cilindros}</p>
    <h6 class="card-subtitle mb-2 text-body-secondary">${car.marca}</h6>
    <p class="card-text"> ${motor.observacao ? motor.observacao : "N/a"} </p>
  </div>
</div>`;
  return asset;
}

/*s nameSearch() {
  let name = $("#search").val().toLowerCase();
  let carsArr = [];

  for (let i = 0; i < cars.length; i++) {
    if (cars[i].modelo.toLowerCase().includes(name)) {
      console.log("nameSearch", cars[i]);

      carsArr.push(cars[i]);
    }
  }

  $("#cars")[0].innerHTML = name;
}*/

//Add a new car
function addNewCar() {
  let motor_id = Number($("#motorID").val());
  let idCar = Number($("#idCar").val());
  let brand = $("#brand").val();
  let model = $("#model").val();
  let color = $("#color").val();

  //testing the all items in motor's and car's array
  let motorExist = motors.some((m) => m.id == motor_id);
  let testCarID = cars.some((c) => c.id == idCar);

  let newCar = {};

  if (motorExist) {
    if (testCarID) {
      for (let i = 0; testCarID && i < cars.length; i++) {
        if (cars[i].id == idCar) {
          testCarID = true;
          idCar += 1;
        }
      }

      console.log("the ID of NewCar is OK:", idCar);

      newCar = {
        id: idCar,
        marca: brand,
        modelo: model,
        cor: color,
        motor_id: motor_id,
      };
      cars.push(newCar);
      carOptions();
      console.log(
        "Car added but this ID already exist! \n New Id added to:'",
        model,
        "' => ID:",
        idCar,
      );
    } else {
      console.log("the ID of NewCar is OK:", idCar);

      newCar = {
        id: idCar,
        marca: brand,
        modelo: model,
        cor: color,
        motor_id: motor_id,
      };
      cars.push(newCar);
      carOptions();
      console.log("New car with Id:", idCar, "added!");
    }
  } else {
    console.error("ERROR");
    alert("This motor ID non exist, please resgister this new Motor infos");
  }
}

//Add new motor
function addNewMotor() {
  let cyllinder = Number($("#cyllinder").val());
  let idMotor = Number($("#idMotor").val());
  let liters = Number($("#liters").val());

  let positionCylinder = $("#positionCylinder").val();
  let obs = $("#obs").val() ? $("#obs").val() : null;

  //testing the all items in motor's and car's array
  let testMotorID = !motors.some((m) => m.id == idMotor);

  let NewMotor = {};

  if (testMotorID) {
    console.log("the ID of NewMotor is OK:", idMotor);

    NewMotor = {
      id: idMotor,
      posicionamento_cilindros: positionCylinder,
      cilindros: cyllinder,
      litragem: liters,
      observacao: obs,
    };
    motors.push(NewMotor);
    carOptions();
    console.log(motors);
  } else {
    console.error("ERROR");
    alert("This motor ID alredy exist, please resgister a new Motor ID");
  }
}

function optionToRemove() {
  let options = "";
  carOptions();
  for (let i = 0; i < cars.length; i++) {
    options += `
          <div class="card w-30">
            <div class="card-body">
              <h2 class="card-title">${cars[i].modelo.toUpperCase()}</h2>
              <p class="card-text">
                <p id="idCar_R">${cars[i].id}</p>
                <p id="brand_R">${cars[i].marca}</p>
                <p id="model_R">${cars[i].modelo}</p>
                <p id="color_R">${cars[i].cor}</p>
                <p id="motorID_R">${cars[i].motor_id}</p>
              </p>
              <button type="button" class="btn btn-danger" data-bs-dismiss="modal" onclick="removeCar(${cars[i].id})">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash"
                  viewBox="0 0 16 16">
                  <path
                    d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                  <path
                    d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                </svg>
                Remove
              </button>
            </div>
          </div>`;
  }
  $("#modalRemove")[0].innerHTML = options;
}
function removeCar(position) {
  console.log("entrou no remove");
  let idPosition = position;

  let motor_id_R = Number($("#motorID_R").text());
  let idCar_R = Number($("#idCar_R").text());
  let brand_R = $("#brand_R").text();
  let model_R = $("#model_R").text();
  let color_R = $("#color_R").text();
  let carToRemove = {
    id: idCar_R,
    marca: brand_R,
    modelo: model_R,
    cor: color_R,
    motor_id: motor_id_R,
  };

  console.log("leu o array:", carToRemove);

  let index = cars.filter((idPosition) => idPosition !== carToRemove);
  console.log("index para apagar-lo", index);

  carOptions();
  if (index != idPosition) {
    cars.splice(index, 1); //splice off in car selected to array
  }
  console.log("na teoria atualizou o:", cars);
  carOptions();
}
