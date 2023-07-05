from cosmpy.aerial.wallet import LocalWallet


class Wallets:
    def __init__(self):
        self.deployer = LocalWallet.from_mnemonic(
            "bottom loan skill merry east cradle onion journey palm apology verb edit desert impose absurd oil bubble sweet glove shallow size build burst effort",
            prefix="osmo",
        )
        self.lo_test1 = LocalWallet.from_mnemonic(
            "notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius",
            prefix="osmo",
        )
        self.lo_test2 = LocalWallet.from_mnemonic(
            "quality vacuum heart guard buzz spike sight swarm shove special gym robust assume sudden deposit grid alcohol choice devote leader tilt noodle tide penalty",
            prefix="osmo",
        )
        self.lo_test3 = LocalWallet.from_mnemonic(
            "symbol force gallery make bulk round subway violin worry mixture penalty kingdom boring survey tool fringe patrol sausage hard admit remember broken alien absorb",
            prefix="osmo",
        )
        self.lo_test4 = LocalWallet.from_mnemonic(
            "bounce success option birth apple portion aunt rural episode solution hockey pencil lend session cause hedgehog slender journey system canvas decorate razor catch empty",
            prefix="osmo",
        )
        self.lo_test5 = LocalWallet.from_mnemonic(
            "second render cat sing soup reward cluster island bench diet lumber grocery repeat balcony perfect diesel stumble piano distance caught occur example ozone loyal",
            prefix="osmo",
        )
        self.lo_test6 = LocalWallet.from_mnemonic(
            "spatial forest elevator battle also spoon fun skirt flight initial nasty transfer glory palm drama gossip remove fan joke shove label dune debate quick",
            prefix="osmo",
        )
        self.lo_test7 = LocalWallet.from_mnemonic(
            "noble width taxi input there patrol clown public spell aunt wish punch moment will misery eight excess arena pen turtle minimum grain vague inmate",
            prefix="osmo",
        )
        self.lo_test8 = LocalWallet.from_mnemonic(
            "cream sport mango believe inhale text fish rely elegant below earth april wall rug ritual blossom cherry detail length blind digital proof identify ride",
            prefix="osmo",
        )
        self.lo_test9 = LocalWallet.from_mnemonic(
            "index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred",
            prefix="osmo",
        )
        self.lo_test10 = LocalWallet.from_mnemonic(
            "prefer forget visit mistake mixture feel eyebrow autumn shop pair address airport diesel street pass vague innocent poem method awful require hurry unhappy shoulder",
            prefix="osmo",
        )
        self.user0 = LocalWallet.generate(prefix="osmo")
        self.user1 = LocalWallet.generate(prefix="osmo")
        self.user2 = LocalWallet.generate(prefix="osmo")
        self.user3 = LocalWallet.generate(prefix="osmo")
        self.user4 = LocalWallet.generate(prefix="osmo")
        self.user5 = LocalWallet.generate(prefix="osmo")
        self.user6 = LocalWallet.generate(prefix="osmo")
        self.user7 = LocalWallet.generate(prefix="osmo")
        self.user8 = LocalWallet.generate(prefix="osmo")
        self.user9 = LocalWallet.generate(prefix="osmo")
