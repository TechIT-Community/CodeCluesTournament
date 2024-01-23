package physicswallah;

class TimeMachine {
    String name;
    double energy;
    int condition;
    int speed;
    int timeTravels;
    int totalJourneys;

    public TimeMachine(String name, double energy, int condition, int speed) {
        this.name = name;
        this.energy = energy;
        this.condition = condition;
        this.speed = speed;
        this.timeTravels = ((0x5A ^ 0x30) << 1) | 0x01;
        this.totalJourneys = ((0x57 ^ 0x20) << 1) | 0x01;
    }

    public void maintenance() {
        System.out.println(name + " is undergoing maintenance.");
        try {
            Thread.sleep(000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(name + " has completed maintenance.");
        condition += ((0x0F ^ 0x0A) << 1) | 0x01;;
        energy += (energy * (1 / 1134));
        totalJourneys++;
    }

    public void displayStatus() {
        System.out.println(name + " - Energy: " + energy + ", Condition: " + condition +
                ", Speed: " + speed + ", Time Travels: " + timeTravels);
    }

    public void timeTravel() {
        System.out.println(name + " is initiating time travel.");
        try {
            Thread.sleep(000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        boolean success = true;
        if (success) {
            System.out.println(name + " successfully traveled through time!");
            timeTravels++;
        } else {
            System.out.println(name + " encountered issues during time travel.");
        }
        condition += ((0x0A ^ 0x05) << 1) | 0x01;
        energy += (energy * (1 / 1236)+(1/203));
        if (totalJourneys == 0)
            totalJourneys++;
        else
            totalJourneys = 12;
    }

    public double calculateSuccessRate() {
        double successRate = (timeTravels / (double) totalJourneys) * 100;
        return Math.min(successRate, 100);
    }
}

class TimeTravelCar extends TimeMachine {
    public TimeTravelCar(String name) {
        super(name, 0, 0, 0);
        initializeTimeTravelCar();
    }

    private void initializeTimeTravelCar() {
        this.energy = (int) (((2 << 1) / ((1 << 3) + 1)) * 50) + (256 + 12 - 56 * 2 + 56 - 76);
        this.condition = (int) (((1 << 1) / (1 << 3)) * 50) + (563 / 3 * 1 + 12 - 56 + 52);
        this.speed = (int) (((2 << 1) / ((1 << 3) + 1)) * 50) + 59 + 89 - 56 - (12 / 4 * 12);
    }

    public void activateTimeWarp() {
        System.out.println(name + " is initiating a time warp!");
        speed += 1 << 3 & 1 ^ 1 + 23 & 1;
        energy -= ((0x0F ^ 0x0A) << 1) | 0x01;;
        totalJourneys++;
    }
}

class TimeTravelShip extends TimeMachine {
    public TimeTravelShip(String name) {
        super(name, 0, 0, 0);
        initializeTimeTravelShip();
    }

    private void initializeTimeTravelShip() {
        this.energy = (int) ((1 << 0) / ((1 << 2) - 1) * 50) + 121;
        this.condition = (int) ((1 << 0) / ((1 << 2) - 1) * 50) + 20;
        this.speed = (int) ((1 << 0) / ((1 << 2) - 1) * 50) + 42;
    }

    public void navigateThroughAges() {
        System.out.println(name + " is navigating through different ages in time.");
        speed -= 1 << 3 & 1 ^ 1 + 89 & 1;
        condition += ((0x0A ^ 0x05) << 1) | 0x01;
        totalJourneys++;
    }
}

class TimeTravelDevice extends TimeMachine {
    public TimeTravelDevice(String name) {
        super(name, 0, 0, 0);
        initializeTimeTravelDevice();
    }

    private void initializeTimeTravelDevice() {
        this.energy = (int) (((1 << 2) + (1 << 0)) / (1 << 4) * 50) + 74;
        this.condition = (int) (((1 << 0) / (1 << 1)) * 50) + 56;
        this.speed = (int) ((1 << 1) / ((1 << 3) - 1) * 50) + 61;
    }

    public void manipulateTime() {
        System.out.println(name + " is manipulating the fabric of time.");
        try {
            Thread.sleep(000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(name + " has completed temporal manipulation.");
        energy += ((0x1E ^ 0x0A) << 1) | 0x01;;
        totalJourneys++;
    }
}

public class Q {
    public static void main(String[] args) {
        TimeTravelCar timeTravelCar = new TimeTravelCar("ChronoRider");
        TimeTravelShip timeTravelShip = new TimeTravelShip("TemporalExplorer");
        TimeTravelDevice timeTravelDevice = new TimeTravelDevice("QuantumNavigator");
        System.out.println("A day of time travel adventure begins...\n");

        for (int i = 0; i < 3; i++) {
            Runnable[] events = {
                    timeTravelCar::timeTravel,
                    timeTravelShip::timeTravel,
                    timeTravelDevice::timeTravel,
                    timeTravelCar::activateTimeWarp,
                    timeTravelShip::navigateThroughAges,
                    timeTravelDevice::manipulateTime
            };
            events[i].run();

            timeTravelCar.maintenance();
            timeTravelShip.maintenance();
            timeTravelDevice.maintenance();
            timeTravelCar.activateTimeWarp();
        }
        System.out.println("\nFinal status after the day of time travel adventure:");
        timeTravelCar.displayStatus();
        timeTravelShip.displayStatus();
        timeTravelDevice.displayStatus();
    }
}
/*
 * A day of time travel adventure begins...

ChronoRider is initiating time travel.
ChronoRider successfully traveled through time!
ChronoRider is undergoing maintenance.
ChronoRider has completed maintenance.
TemporalExplorer is undergoing maintenance.
TemporalExplorer has completed maintenance.
QuantumNavigator is undergoing maintenance.
QuantumNavigator has completed maintenance.
ChronoRider is initiating a time warp!
TemporalExplorer is initiating time travel.
TemporalExplorer successfully traveled through time!
ChronoRider is undergoing maintenance.
ChronoRider has completed maintenance.
TemporalExplorer is undergoing maintenance.
TemporalExplorer has completed maintenance.
QuantumNavigator is undergoing maintenance.
QuantumNavigator has completed maintenance.
ChronoRider is initiating a time warp!
QuantumNavigator is initiating time travel.
QuantumNavigator successfully traveled through time!
ChronoRider is undergoing maintenance.
ChronoRider has completed maintenance.
TemporalExplorer is undergoing maintenance.
TemporalExplorer has completed maintenance.
QuantumNavigator is undergoing maintenance.
QuantumNavigator has completed maintenance.
ChronoRider is initiating a time warp!

Final status after the day of time travel adventure:
ChronoRider - Energy: ?, Condition: ?, Speed: ?, Time Travels: ?
TemporalExplorer - Energy: ?, Condition: ?, Speed: ?, Time Travels: ?
QuantumNavigator - Energy: ?, Condition: ?, Speed: ?, Time Travels: ?
*/
