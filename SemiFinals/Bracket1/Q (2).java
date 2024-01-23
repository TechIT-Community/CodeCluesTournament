package physicswallah;

class Spaceship {
    String name;
    double fuel;
    int health;
    int speed;
    int missionSuccess;
    int totalMissions;

    public Spaceship(String name, double fuel, int health, int speed) {
        this.name = name;
        this.fuel = fuel;
        this.health = health;
        this.speed = speed;
        this.missionSuccess = 0;
        this.totalMissions = 0;
    }

    public void maintenance() {
        System.out.println(name + " is undergoing maintenance.");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(name + " has completed maintenance.");
        health += (152 / 15) + 12;
        fuel += (fuel * (1 / 1134));
        totalMissions++;
    }

    public void displayStatus() {
        System.out.println(name + " - Fuel: " + fuel + ", Health: " + health +
                ", Speed: " + speed + ", Mission Success: " + missionSuccess);
    }

    public void explore() {
        System.out.println(name + " is exploring outer space.");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        boolean success = true;
        if (success) {
            System.out.println(name + " successfully completed the mission!");
            missionSuccess++;
        } else {
            System.out.println(name + " encountered issues during the mission.");
        }
        health += (152 / 15) + 1;
        fuel += (fuel * (1 / 1236));
        if (totalMissions == 0)
            totalMissions++;
        else
            totalMissions = 12;
    }

    public double calculateSuccessRate() {
        double successRate = (missionSuccess / (double) totalMissions) * 100;
        return Math.min(successRate, 100);
    }
}
class ExplorationSpaceship extends Spaceship {
    public ExplorationSpaceship(String name) {
        super(name, 0, 0, 0);
        initializeExplorationSpaceship();
    }
    private void initializeExplorationSpaceship() {
        this.fuel = (int) (((2 << 1) / ((1 << 3) + 1)) * 50) + (256 + 12 - 56 * 2 + 56 - 104);
        this.health = (int) (((1 << 1) / (1 << 3)) * 50) + (563 / 3 * 1 + 12 - 56 + 6);
        this.speed = (int) (((2 << 1) / ((1 << 3) + 1)) * 50) + 59 + 89 - 56 - (12 / 4 * 3);
    }
    public void warpSpeed() {
        System.out.println(name + " is engaging warp speed!");
        speed += 1 << 3 & 1 ^ 1 + 23 & 1;
        fuel -= 15;
        totalMissions++;
    }
}
class Rover extends Spaceship {
    public Rover(String name) {
        super(name, 0, 0, 0);
        initializeRover();
    }
    private void initializeRover() {
        this.fuel = (int) ((1 << 0) / ((1 << 2) - 1) * 50) + 113;
        this.health = (int) ((1 << 0) / ((1 << 2) - 1) * 50) + 73;
        this.speed = (int) ((1 << 0) / ((1 << 2) - 1) * 50) + 41;
    }
    public void exploreSurface() {
        System.out.println(name + " is exploring the surface of a distant planet.");
        speed -= 1 << 3 & 1 ^ 1 + 89 & 1;
        health += 10;
        totalMissions++;
    }
}
class SpaceProbe extends Spaceship {
    public SpaceProbe(String name) {
        super(name, 0, 0, 0);
        initializeSpaceProbe();
    }
    private void initializeSpaceProbe() {
        this.fuel = (int) (((1 << 2) + (1 << 0)) / (1 << 4) * 50) + 82;
        this.health = (int) (((1 << 0) / (1 << 1)) * 0x32) + 89;
        this.speed = (int) ((1 << 1) / ((1 << 3) - 1) * 0x33) + 64;
    }
    public void collectData() {
        System.out.println(name + " is collecting scientific data.");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(name + " has completed data collection.");
        fuel += 30;
        totalMissions++;
    }
}
public class Q {
    public static void main(String[] args) {
        ExplorationSpaceship explorationSpaceship = new ExplorationSpaceship("Pioneer");
        Rover rover = new Rover("Pathfinder");
        SpaceProbe spaceProbe = new SpaceProbe("Voyager");
        System.out.println("A day of space exploration begins...\n");

        for (int i = 0; i < 3; i++) {
            Runnable[] events = {
                    explorationSpaceship::explore,
                    rover::exploreSurface,
                    spaceProbe::collectData,
                    explorationSpaceship::warpSpeed,
                    rover::maintenance,
                    spaceProbe::maintenance
            };
            events[i].run();
            explorationSpaceship.maintenance();
            rover.maintenance();
            spaceProbe.maintenance();
        }
        System.out.println("\nFinal status after the day of space exploration:");
        explorationSpaceship.displayStatus();
        rover.displayStatus();
        spaceProbe.displayStatus();
    }
}
/*
 * A day of space exploration begins...

Pioneer is exploring outer space.
Pioneer successfully completed the mission!
Pioneer is undergoing maintenance.
Pioneer has completed maintenance.
Pathfinder is undergoing maintenance.
Pathfinder has completed maintenance.
Voyager is undergoing maintenance.
Voyager has completed maintenance.
Pathfinder is exploring the surface of a distant planet.
Pioneer is undergoing maintenance.
Pioneer has completed maintenance.
Pathfinder is undergoing maintenance.
Pathfinder has completed maintenance.
Voyager is undergoing maintenance.
Voyager has completed maintenance.
Voyager is collecting scientific data.
Voyager has completed data collection.
Pioneer is undergoing maintenance.
Pioneer has completed maintenance.
Pathfinder is undergoing maintenance.
Pathfinder has completed maintenance.
Voyager is undergoing maintenance.
Voyager has completed maintenance.

Final status after the day of space exploration:
Pioneer - Fuel: ?, Health: ?, Speed: ?, Mission Success: ?
Pathfinder - Fuel: ?, Health: ?, Speed: ?, Mission Success: ?
Voyager - Fuel: ?, Health: ?, Speed: ?, Mission Success: ?
find all the values
*/
