package physicswallah;

import java.util.Random;

class Spaceship {
    String name;
    double fuel;
    int health;
    int shields;
    int experience;
    int successfulActions;
    int totalActions;

    public Spaceship(String name, double fuel, int health, int shields, int experience) {
        this.name = name;
        this.fuel = fuel;
        this.health = health;
        this.shields = shields;
        this.experience = experience;
        this.successfulActions = 0;
        this.totalActions = 0;
    }

    public void repair() {
        System.out.println(name + " is repairing.");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(name + " is fully repaired.");
        health += 20;
        shields += 10;
    }

    public void displayStatus() {
        System.out.println(name + " - Fuel: " + fuel + ", Health: " + health +
                           ", Shields: " + shields + ", Experience: " + experience);
    }

    public void performAction(String action, String successMessage, String failureMessage,
                              Runnable successEffect, Runnable failureEffect) {
        System.out.println(name + " is " + action + ".");
        try {
            Thread.sleep((long) (Math.random() * 2000 + 500));
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        boolean success = new Random().nextBoolean();
        if (success) {
            System.out.println(name + " " + successMessage);
            successEffect.run();
        } else {
            System.out.println(name + " " + failureMessage);
            failureEffect.run();
        }
        totalActions++;
        if (success) {
            successfulActions++;
        }
    }

    public double calculateAverageSuccessRate() {
        return (successfulActions / (double) totalActions) * 100;
    }
}

class Starfighter extends Spaceship {
    public Starfighter(String name, double fuel, int health, int shields, int experience) {
        super(name, fuel, health, shields, experience);
    }

    public void attack() {
        performAction(
                "attacking",
                "successfully attacked!",
                "failed to attack.",
                () -> health = Math.max(0, health - 15),
                () -> shields = Math.max(0, shields - 10)
        );
    }

    public void evasiveManeuver() {
        performAction(
                "performing an evasive maneuver",
                "successfully avoided an enemy attack.",
                "failed to avoid an enemy attack.",
                () -> shields = Math.min(100, shields + 15),
                () -> fuel = Math.max(0, fuel - 5)
        );
    }

    public void upgradeShields() {
        performAction(
                "upgrading shields",
                "successfully upgraded shields!",
                "failed to upgrade shields.",
                () -> shields = Math.min(100, shields + 20),
                () -> experience = Math.max(0, experience - 5)
        );
    }
}

class CargoShip extends Spaceship {
    public CargoShip(String name, double fuel, int health, int shields, int experience) {
        super(name, fuel, health, shields, experience);
    }

    public void loadCargo() {
        performAction(
                "loading cargo",
                "loaded the cargo.",
                "failed to load the cargo.",
                () -> fuel = Math.max(0, fuel - 10),
                () -> health = Math.max(0, health - 5)
        );
    }

    public void unloadCargo() {
        performAction(
                "unloading cargo",
                "successfully unloaded the cargo.",
                "failed to unload the cargo.",
                () -> health = Math.min(100, health + 10),
                () -> shields = Math.max(0, shields - 10)
        );
    }

    public void refuel() {
        performAction(
                "refueling",
                "successfully refueled.",
                "failed to refuel.",
                () -> fuel = Math.min(100, fuel + 20),
                () -> experience = Math.max(0, experience - 5)
        );
    }
}

class ExplorerShip extends Spaceship {
    public ExplorerShip(String name, double fuel, int health, int shields, int experience) {
        super(name, fuel, health, shields, experience);
    }

    public void explore() {
        performAction(
                "exploring",
                "successfully explored.",
                "failed to explore.",
                () -> fuel = Math.max(0, fuel - 15),
                () -> experience = Math.max(0, experience - 10)
        );
    }

    public void collectData() {
        performAction(
                "collecting scientific data",
                "successfully collected valuable data.",
                "failed to collect valuable data.",
                () -> health = Math.min(100, health + 15),
                () -> fuel = Math.max(0, fuel - 10)
        );
    }

    public void gainExperience() {
        performAction(
                "gaining experience",
                "gained valuable experience.",
                "failed to gain experience.",
                () -> experience = Math.min(100, experience + 20),
                () -> fuel = Math.max(0, fuel - 5)
        );
    }
}

public class Q {
    public static void main(String[] args) {
        // Create instances of each spaceship
        Starfighter starfighter = new Starfighter("Fury", 100, 100, 50, 0);
        CargoShip cargoShip = new CargoShip("Phoenix", 150, 120, 50, 0);
        ExplorerShip explorerShip = new ExplorerShip("Odyssey", 200, 80, 50, 0);

        // Simulate a day in space
        System.out.println("A day in space begins...\n");

        // Random events during the day
        for (int i = 0; i < 3; i++) {
            Runnable[] events = {
                    starfighter::attack,
                    starfighter::evasiveManeuver,
                    starfighter::upgradeShields,
                    cargoShip::loadCargo,
                    cargoShip::unloadCargo,
                    cargoShip::refuel,
                    explorerShip::explore,
                    explorerShip::collectData,
                    explorerShip::gainExperience
            };
            events[new Random().nextInt(events.length)].run();

            starfighter.repair();
            cargoShip.repair();
            explorerShip.repair();
        }

        // Display final status and calculations
        System.out.println("\nFinal status after the day in space:");
        starfighter.displayStatus();
        cargoShip.displayStatus();
        explorerShip.displayStatus();
    }
}
/*A day in space begins...

Odyssey is exploring.
Odyssey failed to explore.
Fury is repairing.
Fury is fully repaired.
Phoenix is repairing.
Phoenix is fully repaired.
Odyssey is repairing.
Odyssey is fully repaired.
Fury is attacking.
Fury failed to attack.
Fury is repairing.
Fury is fully repaired.
Phoenix is repairing.
Phoenix is fully repaired.
Odyssey is repairing.

Odyssey is fully repaired.
Phoenix is loading cargo.
Phoenix loaded the cargo.
Fury is repairing.
Fury is fully repaired.
Phoenix is repairing.
Phoenix is fully repaired.
Odyssey is repairing.
Odyssey is fully repaired.*/
//inal status after the day in space