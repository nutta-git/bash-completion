import pytest

from conftest import assert_complete


class TestDoas:
    @pytest.mark.complete("doas -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("doas cd foo", cwd="shared/default")
    def test_2(self, completion):
        assert completion == ".d/"
        assert not completion.endswith(" ")

    @pytest.mark.complete("doas sh share")
    def test_3(self, completion):
        assert completion == "d/"
        assert not completion.endswith(" ")

    @pytest.mark.complete("doas mount /dev/sda1 def", cwd="shared")
    def test_4(self, completion):
        assert completion == "ault/"
        assert not completion.endswith(" ")

    @pytest.mark.complete("doas -e -u root bar foo", cwd="shared/default")
    def test_5(self, completion):
        assert completion == "foo foo.d/".split()

    def test_6(self, bash, part_full_user):
        part, full = part_full_user
        completion = assert_complete(bash, "doas chown %s" % part)
        assert completion == full[len(part) :]
        assert completion.endswith(" ")

    def test_7(self, bash, part_full_user, part_full_group):
        _, user = part_full_user
        partgroup, fullgroup = part_full_group
        completion = assert_complete(
            bash, "doas chown %s:%s" % (user, partgroup)
        )
        assert completion == fullgroup[len(partgroup) :]
        assert completion.endswith(" ")

    def test_8(self, bash, part_full_group):
        part, full = part_full_group
        completion = assert_complete(bash, "sudo chown dot.user:%s" % part)
        assert completion == full[len(part) :]
        assert completion.endswith(" ")

    @pytest.mark.parametrize(
        "prefix",
        [
            r"funky\ user:",
            "funky.user:",
            r"funky\.user:",
            r"fu\ nky.user:",
            r"f\ o\ o\.\bar:",
            r"foo\_b\ a\.r\ :",
        ],
    )
    def test_9(self, bash, part_full_group, prefix):
        """Test preserving special chars in $prefix$partgroup<TAB>."""
        part, full = part_full_group
        completion = assert_complete(bash, "sudo chown %s%s" % (prefix, part))
        assert completion == full[len(part) :]
        assert completion.endswith(" ")

    def test_10(self, bash, part_full_user, part_full_group):
        """Test giving up on degenerate cases instead of spewing junk."""
        _, user = part_full_user
        partgroup, _ = part_full_group
        for x in range(2, 5):
            completion = assert_complete(
                bash, "sudo chown %s%s:%s" % (user, x * "\\", partgroup)
            )
            assert not completion

    def test_11(self, bash, part_full_group):
        """Test graceful fail on colon in user/group name."""
        part, _ = part_full_group
        completion = assert_complete(bash, "sudo chown foo:bar:%s" % part)
        assert not completion
